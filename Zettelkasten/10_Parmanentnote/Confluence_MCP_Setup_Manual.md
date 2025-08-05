# Confluence MCP Tools セットアップマニュアル

## 📋 **概要**
Cursorで自然言語によりConfluence内の情報を検索・質問できるMCP Toolsの設定手順です。セキュリティを重視し、個人スペースのみにアクセスを制限した設定になっています。

## 🔧 **前提条件**

### 必要な情報
- **Confluence Cloud URL**: `https://your-company.atlassian.net`
- **メールアドレス**: Confluenceアカウントのメール
- **APIトークン**: Confluence API用（後述の手順で取得）
- **個人スペース名**: 自分の個人スペース名（通常は名前）

### 必要なソフトウェア
- **Cursor**: 最新版
- **Python 3**: `python3 --version` で確認
- **httpx**: `python3 -m pip install httpx`

## 🚀 **セットアップ手順**

### Step 1: APIトークンの取得

1. **Confluence Cloud** にログイン
2. **右上のプロフィール** → **アカウント設定**
3. **セキュリティ** → **APIトークンを作成および管理**
4. **APIトークンを作成** をクリック
5. **ラベル名**: `Cursor MCP Tool`
6. **作成** をクリックしてトークンをコピー

### Step 2: 必要なディレクトリの作成

```bash
mkdir -p ~/.cursor/mcp_servers
```

### Step 3: 設定ファイルの作成

#### 3-1. confluence_config.json

```bash
# 設定ファイルを作成
nano ~/.cursor/mcp_servers/confluence_config.json
```

以下を入力（**実際の値に置き換え**）：

```json
{
    "confluence_url": "https://your-company.atlassian.net",
    "email": "your-email@company.com",
    "api_token": "YOUR_API_TOKEN_HERE", 
    "default_space": "ACTUAL_SPACE_KEY_HERE",
    "security_level": "maximum_restricted",
    "allowed_spaces": ["ACTUAL_SPACE_KEY_HERE"],
    "blocked_spaces": "ALL_EXCEPT_personal_space",
    "usage_purpose": "個人スペースの1on1記録のみ - 他のスペースは完全にブロック",
    "space_name": "your_name",
    "actual_space_key": "ACTUAL_SPACE_KEY_HERE"
}
```

#### 3-2. 設定ファイルのセキュリティ設定

```bash
chmod 600 ~/.cursor/mcp_servers/confluence_config.json
```

### Step 4: 個人スペースキーの特定

個人スペースキーは通常 `~` で始まる長い英数字です。以下のスクリプトで特定します：

```bash
# スペース確認スクリプトを作成
nano ~/.cursor/mcp_servers/find_space.py
```

以下を入力：

```python
#!/usr/bin/env python3
import json
import asyncio
import httpx
import base64

async def find_personal_space():
    # 設定読み込み
    with open("/Users/YOUR_USERNAME/.cursor/mcp_servers/confluence_config.json", 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    auth_string = f"{config['email']}:{config['api_token']}"
    auth_bytes = auth_string.encode('ascii')
    auth_b64 = base64.b64encode(auth_bytes).decode('ascii')
    
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        url = f"{config['confluence_url']}/wiki/rest/api/space"
        params = {"limit": 100}
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        spaces_data = response.json()
        
        print("=== 利用可能なスペース一覧 ===")
        personal_spaces = []
        
        for space in spaces_data.get('results', []):
            space_key = space.get('key', 'Unknown')
            space_name = space.get('name', 'Unknown')
            print(f"- {space_key}: {space_name}")
            
            if space_key.startswith('~'):
                personal_spaces.append((space_key, space_name))
        
        print(f"\n=== 個人スペース（候補） ===")
        for key, name in personal_spaces:
            print(f"- {key}: {name}")
            if "your_name" in name.lower():  # your_nameを実際の名前に変更
                print(f"  *** これがあなたのスペースの可能性が高いです ***")

if __name__ == "__main__":
    asyncio.run(find_personal_space())
```

実行して個人スペースキーを特定：

```bash
python3 ~/.cursor/mcp_servers/find_space.py
```

**出力例**：
```
- ~7120209bbb450ded7247dbb5c64f32d1a85791: your_name
  *** これがあなたのスペースの可能性が高いです ***
```

### Step 5: 設定ファイルの更新

特定したスペースキーで `confluence_config.json` を更新：

```json
{
    "confluence_url": "https://your-company.atlassian.net",
    "email": "your-email@company.com",
    "api_token": "YOUR_API_TOKEN_HERE", 
    "default_space": "~7120209bbb450ded7247dbb5c64f32d1a85791",
    "security_level": "maximum_restricted",
    "allowed_spaces": ["~7120209bbb450ded7247dbb5c64f32d1a85791"],
    "blocked_spaces": "ALL_EXCEPT_personal_space",
    "usage_purpose": "個人スペースの1on1記録のみ - 他のスペースは完全にブロック",
    "space_name": "your_name",
    "actual_space_key": "~7120209bbb450ded7247dbb5c64f32d1a85791"
}
```

### Step 6: MCPサーバーファイルの作成

```bash
nano ~/.cursor/mcp_servers/secure_confluence_mcp_server.py
```

以下の完全なコードを入力：

```python
#!/usr/bin/env python3
"""
Secure Confluence MCP Server
個人スペース専用・セキュリティ制御付きConfluence検索ツール
"""

import sys
import json
import asyncio
import httpx
import base64
import re
from typing import Optional, Dict, Any, List

class SecureConfluenceMCPServer:
    def __init__(self):
        self.max_content_length = 500
        self.sensitive_keywords = [
            "password", "token", "key", "secret", "confidential",
            "パスワード", "機密", "秘密", "トークン"
        ]
        
        # 設定読み込み
        try:
            with open(f"{sys.path[0]}/confluence_config.json", 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            with open("/Users/h_yara/.cursor/mcp_servers/confluence_config.json", 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        
        # Basic認証の設定
        auth_string = f"{self.config['email']}:{self.config['api_token']}"
        auth_bytes = auth_string.encode('ascii')
        self.auth_header = base64.b64encode(auth_bytes).decode('ascii')
    
    def sanitize_content(self, content: str) -> str:
        """コンテンツのサニタイズ"""
        if not content:
            return ""
        
        # HTMLタグを除去
        clean_content = re.sub(r'<[^>]+>', '', content)
        clean_content = clean_content.replace('&nbsp;', ' ').replace('&amp;', '&')
        
        # 機密キーワードのフィルタリング
        for keyword in self.sensitive_keywords:
            if keyword.lower() in clean_content.lower():
                return "[機密情報のため非表示]"
        
        # 長さ制限
        if len(clean_content) > self.max_content_length:
            clean_content = clean_content[:self.max_content_length] + "..."
        
        return clean_content.strip()
    
    async def secure_search_confluence(self, query: str, space: Optional[str] = None, limit: int = 5) -> Dict[str, Any]:
        """Search Confluence with security filtering - personal space ONLY"""
        # 正しい個人スペースキーを使用
        space_key = self.config['actual_space_key']
        
        # 他のスペースが指定された場合はエラー
        if space and space.lower() != self.config['space_name'].lower():
            return {
                "query": "[アクセス拒否]",
                "space": space,
                "total_results": 0,
                "results": [],
                "security_notice": f"セキュリティ制限: {self.config['space_name']}スペース以外（{space}）へのアクセスは禁止されています"
            }
        
        # 機密性の高いクエリをチェック
        sensitive_query = any(keyword.lower() in query.lower() for keyword in self.sensitive_keywords)
        
        if sensitive_query:
            return {
                "query": "[検索クエリは表示されません]",
                "space": space_key,
                "total_results": 0,
                "results": [],
                "security_notice": "機密情報の検索は制限されています"
            }
        
        # CQLクエリを構築
        cql_query = f'space = "{space_key}" AND text ~ "{query}"'
        
        async with httpx.AsyncClient() as client:
            try:
                url = f"{self.config['confluence_url']}/wiki/rest/api/search"
                headers = {
                    "Authorization": f"Basic {self.auth_header}",
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                }
                params = {
                    "cql": cql_query,
                    "limit": min(limit, 5),
                    "expand": "content.space,content.history.lastUpdated"
                }
                
                response = await client.get(url, headers=headers, params=params)
                response.raise_for_status()
                data = response.json()
                
                results = []
                for result in data.get("results", []):
                    content = result.get("content", {})
                    if content:
                        safe_result = {
                            "title": content.get("title", ""),
                            "type": content.get("type", ""),
                            "space": content.get("space", {}).get("name", ""),
                            "last_updated": content.get("history", {}).get("lastUpdated", {}).get("when", ""),
                            "excerpt": self.sanitize_content(result.get("excerpt", ""))
                        }
                        results.append(safe_result)
                
                return {
                    "query": query,
                    "space": space_key,
                    "total_results": min(data.get("totalSize", 0), 5),
                    "results": results,
                    "security_notice": "セキュリティのため、結果は制限されています"
                }
                
            except Exception as e:
                return {
                    "query": query,
                    "space": space_key,
                    "total_results": 0,
                    "results": [],
                    "error": f"検索エラー: {str(e)}"
                }
    
    async def secure_answer_question(self, question: str, space: Optional[str] = None) -> Dict[str, Any]:
        """質問に対してセキュアに回答"""
        search_keywords = question.replace("?", "").replace("。", "").replace("、", " ")
        # 正しい個人スペースキーで検索
        search_results = await self.secure_search_confluence(search_keywords, self.config['space_name'], limit=3)
        
        if not search_results.get("results") or len(search_results.get("results", [])) == 0:
            return {
                "question": question,
                "answer": "申し訳ございませんが、質問に関連する情報が個人スペースで見つかりませんでした。",
                "sources": [],
                "search_query": search_keywords
            }
        
        # 回答の生成
        answer_parts = [f"「{question}」に関する情報を検索しました。以下の関連ページが見つかりました：\n"]
        sources = []
        
        for i, result in enumerate(search_results["results"], 1):
            title = result.get("title", "不明")
            space_name = result.get("space", "不明")
            last_updated = result.get("last_updated", "不明")
            excerpt = result.get("excerpt", "")
            
            answer_parts.append(f"**{i}. {title}**")
            answer_parts.append(f"スペース: {space_name}")
            answer_parts.append(f"更新日: {last_updated}")
            answer_parts.append(f"内容抜粋: {excerpt}")
            answer_parts.append("📄 詳細は直接Confluenceでご確認ください\n")
            
            sources.append({
                "title": title,
                "space": space_name,
                "last_updated": last_updated
            })
        
        answer_parts.append("\n⚠️ セキュリティのため、詳細な内容表示は制限されています。")
        
        return {
            "question": question,
            "answer": "\n".join(answer_parts),
            "sources": sources,
            "search_query": search_keywords
        }
    
    def create_response(self, id_val, result):
        """JSON-RPC 2.0 レスポンスを作成"""
        return json.dumps({
            "jsonrpc": "2.0",
            "id": id_val,
            "result": result
        })
    
    def create_error_response(self, id_val, code, message):
        """エラーレスポンスを作成"""
        return json.dumps({
            "jsonrpc": "2.0",
            "id": id_val,
            "error": {"code": code, "message": message}
        })
    
    async def handle_initialize(self, params, id_val):
        """初期化ハンドラ"""
        result = {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "secure-confluence-mcp",
                "version": "1.0.0"
            }
        }
        return self.create_response(id_val, result)
    
    async def handle_tools_list(self, params, id_val):
        """利用可能なツールのリスト"""
        tools = [
            {
                "name": "secure_search_confluence",
                "description": f"{self.config['space_name']}スペース専用セキュア検索 - 指定されたキーワードでConfluenceページを検索します",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "検索キーワード"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "secure_ask_confluence",
                "description": f"{self.config['space_name']}スペース専用セキュア質問応答 - 自然言語でConfluence内の情報について質問します",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "質問内容"
                        }
                    },
                    "required": ["question"]
                }
            }
        ]
        
        result = {"tools": tools}
        return self.create_response(id_val, result)
    
    async def handle_tools_call(self, params, id_val):
        """ツール呼び出しハンドラ"""
        try:
            name = params.get("name")
            arguments = params.get("arguments", {})
            
            if name == "secure_search_confluence":
                query = arguments.get("query", "")
                search_result = await self.secure_search_confluence(query)
                content = [{"type": "text", "text": json.dumps(search_result, ensure_ascii=False, indent=2)}]
                
            elif name == "secure_ask_confluence":
                question = arguments.get("question", "")
                answer_result = await self.secure_answer_question(question)
                content = [{"type": "text", "text": answer_result["answer"]}]
                
            else:
                return self.create_error_response(id_val, -32601, f"Unknown tool: {name}")
            
            result = {"content": content}
            return self.create_response(id_val, result)
            
        except Exception as e:
            return self.create_error_response(id_val, -32603, f"Tool execution error: {str(e)}")
    
    async def handle_request(self, request_data):
        """リクエストハンドラ"""
        try:
            method = request_data.get("method")
            params = request_data.get("params", {})
            id_val = request_data.get("id")
            
            if method == "initialize":
                return await self.handle_initialize(params, id_val)
            elif method == "tools/list":
                return await self.handle_tools_list(params, id_val)
            elif method == "tools/call":
                return await self.handle_tools_call(params, id_val)
            else:
                return self.create_error_response(id_val, -32601, f"Unknown method: {method}")
                
        except Exception as e:
            return self.create_error_response(None, -32603, f"Internal error: {str(e)}")

async def main():
    server = SecureConfluenceMCPServer()
    
    for line in sys.stdin:
        if line.strip():
            try:
                request = json.loads(line.strip())
                response = await server.handle_request(request)
                print(response)
                sys.stdout.flush()
            except json.JSONDecodeError:
                error_response = server.create_error_response(None, -32700, "Parse error")
                print(error_response)
                sys.stdout.flush()

if __name__ == "__main__":
    asyncio.run(main())
```

### Step 7: Cursor設定の更新

#### 7-1. settings.json の更新

```bash
# Cursor設定ファイルを開く
nano "/Users/$(whoami)/Library/Application Support/Cursor/User/settings.json"
```

`mcpServers` セクションを追加または更新：

```json
{
    "mcpServers": {
        "confluence": {
            "command": "python3",
            "args": [
                "/Users/YOUR_USERNAME/.cursor/mcp_servers/secure_confluence_mcp_server.py"
            ],
            "disabled": false,
            "autoApprove": ["secure_search_confluence", "secure_ask_confluence"]
        }
    }
}
```

#### 7-2. グローバル設定ファイルの作成

```bash
nano ~/.cursor/mcp.json
```

以下を入力：

```json
{
    "mcpServers": {
        "confluence": {
            "command": "python3",
            "args": [
                "/Users/YOUR_USERNAME/.cursor/mcp_servers/secure_confluence_mcp_server.py"
            ],
            "disabled": false,
            "autoApprove": ["secure_search_confluence", "secure_ask_confluence"]
        }
    }
}
```

### Step 8: 動作テスト

```bash
# MCPサーバーの動作テスト
echo '{"jsonrpc": "2.0", "id": "1", "method": "tools/list", "params": {}}' | python3 ~/.cursor/mcp_servers/secure_confluence_mcp_server.py
```

### Step 9: Cursor再起動

1. **Cursor完全終了**（Cmd+Q）
2. **5秒待って再起動**
3. **新しいチャットで動作確認**

## 🧪 **動作確認**

Cursor の新しいチャットで以下を試す：

```
あなたのスペース内で「議事録」について教えて
```

```
2024年の会議内容を検索して
```

## 🔐 **セキュリティ機能**

### 実装済みセキュリティ
- ✅ **個人スペース専用**: 他のスペースは完全にブロック
- ✅ **機密キーワードフィルタ**: password, token, 機密 等を自動検出
- ✅ **内容長制限**: 500文字以内に制限
- ✅ **HTMLタグ除去**: セキュアなテキストのみ表示
- ✅ **設定ファイル保護**: 600権限で機密情報を保護

### 制限事項
- 個人スペース以外は検索不可
- 結果は最大5件まで
- 機密キーワード含むコンテンツは非表示
- 詳細URLは表示されない

## 🛠️ **トラブルシューティング**

### よくある問題

#### 1. "0 tools enabled" が表示される
- Cursor を完全再起動
- `settings.json` の JSON文法をチェック
- パスが正しいか確認

#### 2. 検索結果が0件
- スペースキーが正しいか確認
- APIトークンの有効性をチェック
- Step 4のスクリプトで再確認

#### 3. APIエラー
- APIトークンを再生成
- メールアドレスが正しいか確認
- Confluence URLが正しいか確認

#### 4. Python モジュールエラー
```bash
python3 -m pip install httpx
```

## 📝 **カスタマイズ方法**

### セキュリティレベルの調整

`secure_confluence_mcp_server.py` 内で調整可能：

```python
# より厳しい制限
self.max_content_length = 200
self.sensitive_keywords.extend(["プロジェクト名", "顧客名"])

# より緩い制限  
self.max_content_length = 1000
```

### 検索結果数の変更

```python
# デフォルトの結果数を変更
async def secure_search_confluence(self, query: str, space: Optional[str] = None, limit: int = 10):
```

## ⚠️ **注意事項**

1. **APIトークンの管理**: 定期的な更新を推奨
2. **設定ファイルの保護**: 他人にアクセスされないよう注意
3. **個人スペース専用**: 会社の機密情報にはアクセスしない設計
4. **利用規約遵守**: 会社のIT利用規約を確認して使用

## 🎯 **完了チェックリスト**

- [x] APIトークン取得完了
- [x] 個人スペースキー特定完了
- [x] 設定ファイル作成完了（600権限設定済み）
- [x] MCPサーバーファイル作成完了
- [x] Cursor設定更新完了
- [x] 動作テスト成功
- [x] セキュリティ設定確認完了

## 🆘 **サポート**

問題が発生した場合は、以下の情報と共にサポートを求めてください：

1. エラーメッセージの詳細
2. 使用しているOS
3. Python バージョン（`python3 --version`）
4. Cursor バージョン
5. 実行したコマンドと結果

---

**🎉 セットアップ完了後は、Confluenceの個人スペースを自然言語で検索できるようになります！** 