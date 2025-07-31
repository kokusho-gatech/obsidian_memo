#!/usr/bin/env python3
import json
import asyncio
import httpx
import base64

async def find_personal_space():
    # 設定読み込み
    with open("/Users/t_kokusho/.cursor/mcp_servers/confluence_config.json", 'r', encoding='utf-8') as f:
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
            if "t_kokusho" in name.lower():
                print(f"  *** これがあなたのスペースの可能性が高いです ***")

if __name__ == "__main__":
    asyncio.run(find_personal_space()) 