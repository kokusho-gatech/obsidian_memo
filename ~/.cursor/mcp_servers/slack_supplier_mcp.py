#!/usr/bin/env python3
"""
Slack MCP Tool for SUPPLIER team
SUPPLIERチーム用のSlack情報検索・質問応答ツール
"""

import os
import json
import asyncio
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
import subprocess

from mcp.server.models import InitializationOptions
from mcp.server.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)

# Slack設定 (実際の値は環境変数または設定ファイルから取得)
SLACK_CONFIG = {
    "team_channels": [
        "#supplier-team",
        "#supplier-dev", 
        "#supplier-pm",
        "#supplier-alerts"
    ],
    "important_keywords": [
        "プロジェクト",
        "リリース",
        "障害",
        "査定",
        "仲介",
        "契約",
        "エラー",
        "バグ",
        "改修",
        "仕様変更"
    ]
}

server = Server("slack-supplier-mcp")

class SlackSupplierMCP:
    def __init__(self):
        self.cache_file = os.path.expanduser("~/.cursor/slack_supplier_cache.json")
        self.log_file = os.path.expanduser("~/.cursor/auto_execution_history.csv")
        
    def log_execution(self, command: str, content: str, result: str):
        """実行ログを記録"""
        now = datetime.now()
        date_str = now.strftime("%Y/%m/%d")
        time_str = now.strftime("%H:%M")
        
        log_entry = f'{date_str},{time_str},Slack情報検索,SUPPLIER Slack,Slack Channel Search,mcp_slack_search(),{content},{result}\n'
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            pass  # ログ記録エラーは無視
    
    def get_cached_data(self) -> Dict[str, Any]:
        """キャッシュされたSlackデータを取得"""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return {}
    
    def save_cached_data(self, data: Dict[str, Any]):
        """Slackデータをキャッシュに保存"""
        try:
            os.makedirs(os.path.dirname(self.cache_file), exist_ok=True)
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception:
            pass
    
    def search_slack_messages(self, query: str, channel: str = None, days_back: int = 7) -> Dict[str, Any]:
        """Slackメッセージの検索（サンプル実装）"""
        # 実際の実装では Slack API を使用
        # ここではサンプルデータを返す
        
        sample_messages = [
            {
                "channel": "#supplier-team",
                "user": "PM_田中",
                "timestamp": "2025-01-30T15:30:00Z",
                "text": f"査定自動化Ph.1の要件定義が完了しました。来週から開発着手予定です。",
                "thread_replies": 3,
                "reactions": ["👍", "🎉"]
            },
            {
                "channel": "#supplier-dev",
                "user": "Dev_佐藤",
                "timestamp": "2025-01-29T10:15:00Z", 
                "text": f"仲介マスタの検索パフォーマンスが改善されました。平均レスポンス時間が500ms→200msに短縮。",
                "thread_replies": 5,
                "reactions": ["💪", "🚀"]
            },
            {
                "channel": "#supplier-team",
                "user": "QA_鈴木",
                "timestamp": "2025-01-28T14:20:00Z",
                "text": f"契約書テンプレート機能でバグを発見。DocuSign連携時にファイル名が文字化けする件。",
                "thread_replies": 8,
                "reactions": ["🐛", "👀"]
            }
        ]
        
        # クエリによるフィルタリング（簡易実装）
        filtered_messages = []
        query_lower = query.lower()
        
        for msg in sample_messages:
            if (query_lower in msg["text"].lower() or 
                (channel and channel.lower() in msg["channel"].lower()) or
                not query_lower):  # 空のクエリは全件返す
                filtered_messages.append(msg)
        
        result = {
            "query": query,
            "channel_filter": channel,
            "days_back": days_back,
            "total_messages": len(filtered_messages),
            "messages": filtered_messages[:10],  # 最大10件
            "summary": self._generate_message_summary(filtered_messages)
        }
        
        self.log_execution(
            "slack_search",
            f"検索クエリ: {query}, チャンネル: {channel or '全体'}, 期間: {days_back}日",
            f"{len(filtered_messages)}件のメッセージを取得"
        )
        
        return result
    
    def _generate_message_summary(self, messages: List[Dict]) -> Dict[str, Any]:
        """メッセージの要約を生成"""
        if not messages:
            return {"themes": [], "key_decisions": [], "action_items": []}
        
        # 簡易的な要約生成
        channels = set(msg["channel"] for msg in messages)
        users = set(msg["user"] for msg in messages)
        
        themes = []
        key_decisions = []
        action_items = []
        
        for msg in messages:
            text = msg["text"].lower()
            if any(keyword in text for keyword in ["査定", "自動化"]):
                themes.append("査定自動化")
            if any(keyword in text for keyword in ["仲介", "マスタ"]):
                themes.append("仲介管理")
            if any(keyword in text for keyword in ["契約", "docusign"]):
                themes.append("契約管理")
            
            if "決定" in text or "承認" in text:
                key_decisions.append({
                    "decision": msg["text"][:100] + "...",
                    "timestamp": msg["timestamp"],
                    "user": msg["user"]
                })
            
            if "TODO" in text or "来週" in text or "予定" in text:
                action_items.append({
                    "action": msg["text"][:100] + "...", 
                    "timestamp": msg["timestamp"],
                    "user": msg["user"]
                })
        
        return {
            "active_channels": list(channels),
            "active_users": list(users),
            "themes": list(set(themes)),
            "key_decisions": key_decisions[:5],
            "action_items": action_items[:5]
        }
    
    def ask_slack_context(self, question: str) -> Dict[str, Any]:
        """Slack上の情報を元に質問に回答"""
        # 実際の実装では RAG や LLM を使用
        # ここではサンプル回答を生成
        
        question_lower = question.lower()
        
        if "査定" in question_lower and "自動化" in question_lower:
            answer = {
                "question": question,
                "answer": "査定自動化Ph.1プロジェクトは現在要件定義が完了し、来週から開発着手予定です。機械学習モデルを活用した査定の効率化が目標で、PM田中さんが進捗管理を担当しています。",
                "relevant_messages": [
                    {
                        "channel": "#supplier-team",
                        "user": "PM_田中", 
                        "text": "査定自動化Ph.1の要件定義が完了しました。来週から開発着手予定です。",
                        "timestamp": "2025-01-30T15:30:00Z"
                    }
                ],
                "confidence": 0.85
            }
        elif "仲介" in question_lower:
            answer = {
                "question": question,
                "answer": "仲介マスタについては最近パフォーマンス改善が実施され、検索レスポンス時間が500ms→200msに短縮されました。データ品質向上のプロジェクトも完了しています。",
                "relevant_messages": [
                    {
                        "channel": "#supplier-dev",
                        "user": "Dev_佐藤",
                        "text": "仲介マスタの検索パフォーマンスが改善されました。平均レスポンス時間が500ms→200msに短縮。",
                        "timestamp": "2025-01-29T10:15:00Z"
                    }
                ],
                "confidence": 0.90
            }
        elif "バグ" in question_lower or "問題" in question_lower:
            answer = {
                "question": question,
                "answer": "最近発見された主要な問題として、契約書テンプレート機能でDocuSign連携時にファイル名が文字化けする件があります。QA_鈴木さんが報告し、現在調査中です。",
                "relevant_messages": [
                    {
                        "channel": "#supplier-team",
                        "user": "QA_鈴木",
                        "text": "契約書テンプレート機能でバグを発見。DocuSign連携時にファイル名が文字化けする件。",
                        "timestamp": "2025-01-28T14:20:00Z"
                    }
                ],
                "confidence": 0.80
            }
        else:
            answer = {
                "question": question,
                "answer": "申し訳ございませんが、該当する情報がSlackの履歴から見つかりませんでした。より具体的なキーワードで検索いただくか、#supplier-teamチャンネルで直接質問してみてください。",
                "relevant_messages": [],
                "confidence": 0.10
            }
        
        self.log_execution(
            "slack_ask",
            f"質問: {question}",
            f"回答生成（信頼度: {answer['confidence']}）"
        )
        
        return answer

# MCPツールの実装
slack_mcp = SlackSupplierMCP()

@server.list_tools()
async def handle_list_tools() -> List[Tool]:
    """利用可能なツール一覧を返す"""
    return [
        Tool(
            name="mcp_slack_search_supplier",
            description="SUPPLIERチーム用Slack検索 - 指定されたキーワードでSlackメッセージを検索します",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "検索キーワード"
                    },
                    "channel": {
                        "type": "string", 
                        "description": "検索対象チャンネル（オプション）"
                    },
                    "days_back": {
                        "type": "integer",
                        "description": "検索期間（日数、デフォルト7日）",
                        "default": 7
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="mcp_slack_ask_supplier",
            description="SUPPLIERチーム用Slack質問応答 - Slack上の情報を元に自然言語で質問に回答します",
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "質問内容"
                    }
                },
                "required": ["question"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """ツール実行を処理"""
    try:
        if name == "mcp_slack_search_supplier":
            query = arguments.get("query", "")
            channel = arguments.get("channel")
            days_back = arguments.get("days_back", 7)
            
            result = slack_mcp.search_slack_messages(query, channel, days_back)
            
            return [TextContent(
                type="text",
                text=json.dumps(result, ensure_ascii=False, indent=2)
            )]
            
        elif name == "mcp_slack_ask_supplier":
            question = arguments.get("question", "")
            
            result = slack_mcp.ask_slack_context(question)
            
            return [TextContent(
                type="text", 
                text=json.dumps(result, ensure_ascii=False, indent=2)
            )]
        
        else:
            return [TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]
            
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error executing tool {name}: {str(e)}"
        )]

async def main():
    # Stdio transport を使用してサーバーを実行
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="slack-supplier-mcp",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main()) 