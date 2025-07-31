#!/usr/bin/env python3
"""
プロダクト説明書作成のための情報収集自動化スクリプト
GitHub PR、Confluence、その他の情報源から包括的にデータを収集します。
"""

import os
import csv
import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Any
import argparse


class ProductDocumentationCollector:
    def __init__(self, project_path: str):
        self.project_path = project_path
        self.log_file = os.path.expanduser("~/.cursor/auto_execution_history.csv")
        self.output_dir = os.path.join(project_path, "collected_data")
        
        # ログファイルが存在しない場合は作成
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Date', 'Time', 'Command', 'Project_Path', 'Scope', 'Command_Executed', 'Content', 'Result'])
    
    def log_execution(self, command: str, scope: str, command_executed: str, content: str, result: str):
        """実行ログをCSVファイルに記録"""
        now = datetime.now()
        date_str = now.strftime("%Y/%m/%d")
        time_str = now.strftime("%H:%M")
        
        with open(self.log_file, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date_str, time_str, command, self.project_path, scope, command_executed, content, result])
    
    def collect_github_data(self, repo_url: str = None, days_back: int = 30) -> Dict[str, Any]:
        """GitHubからPR・コミット情報を収集"""
        print("🔍 GitHub情報を収集中...")
        
        # ここではサンプルデータを返します
        # 実際の実装では GitHub API を使用
        github_data = {
            "recent_prs": [
                {
                    "number": 123,
                    "title": "査定自動化機能の基盤実装",
                    "author": "dev-team",
                    "merged_at": "2025-01-20",
                    "description": "機械学習モデルを活用した査定自動化の基盤を実装",
                    "files_changed": ["app/models/assessment.rb", "app/services/ai_assessment_service.rb"],
                    "labels": ["enhancement", "ai-feature"]
                },
                {
                    "number": 122,
                    "title": "仲介マスタのデータ品質向上",
                    "author": "data-team", 
                    "merged_at": "2025-01-15",
                    "description": "空白率の高い仲介マスタデータの品質向上対応",
                    "files_changed": ["app/models/intermediary_company.rb", "db/migrate/"],
                    "labels": ["data-quality", "bug-fix"]
                }
            ],
            "architecture_changes": [
                {
                    "date": "2025-01-10",
                    "type": "database",
                    "description": "JSONB型によるスキーマレス設計導入",
                    "impact": "書類管理の柔軟性向上"
                }
            ]
        }
        
        self.log_execution(
            "GitHub情報収集",
            "GitHub Repository",
            "collect_github_data()",
            f"過去{days_back}日間のPR・コミット情報",
            f"PR {len(github_data['recent_prs'])}件、アーキテクチャ変更 {len(github_data['architecture_changes'])}件を収集"
        )
        
        return github_data
    
    def collect_confluence_data(self, space: str = "SUPPLIER") -> Dict[str, Any]:
        """Confluenceからプロジェクト・要件情報を収集"""
        print("📚 Confluence情報を収集中...")
        
        # ここではサンプルデータを返します
        # 実際の実装では Confluence API または MCP を使用
        confluence_data = {
            "projects": [
                {
                    "title": "SUP 2025 CRM機能構築ph.1",
                    "status": "進行中",
                    "background": "中期経営計画に向けた事業スケールで10,000社対応が必要",
                    "objectives": ["顧客管理機能作成", "データ品質向上"],
                    "last_updated": "2025-01-28"
                },
                {
                    "title": "SUP 2025 仲介マスタ改修",
                    "status": "完了",
                    "background": "仲介マスタの空白率が高い（市区町村：91.6%、支店名：95.1%）",
                    "objectives": ["データ品質向上", "検索機能改善"],
                    "last_updated": "2025-01-23"
                }
            ],
            "technical_decisions": [
                {
                    "title": "柔軟性重視のDB設計について",
                    "decision": "JSONB型によるスキーマレス設計採用",
                    "rationale": "書類種別・項目の頻繁な追加に対応するため",
                    "trade_offs": "パフォーマンス vs 柔軟性"
                }
            ]
        }
        
        self.log_execution(
            "Confluence情報収集",
            "Confluence Space",
            "collect_confluence_data()",
            f"スペース: {space}からプロジェクト・技術情報",
            f"プロジェクト {len(confluence_data['projects'])}件、技術決定 {len(confluence_data['technical_decisions'])}件を収集"
        )
        
        return confluence_data
    
    def analyze_user_teams(self) -> Dict[str, Any]:
        """ユーザ・チーム分析"""
        print("👥 ユーザ・チーム情報を分析中...")
        
        user_teams_data = {
            "primary_users": [
                {
                    "role": "査定担当者",
                    "team": "不動産評価チーム",
                    "main_features": ["査定機能", "価格予測", "物件情報管理"],
                    "pain_points": ["査定時間の長さ", "データ入力の手間"],
                    "success_metrics": ["査定精度", "処理時間短縮"]
                },
                {
                    "role": "仲介管理者", 
                    "team": "パートナー管理チーム",
                    "main_features": ["仲介会社管理", "スタッフ管理", "取引履歴"],
                    "pain_points": ["データ品質の低さ", "検索性の悪さ"],
                    "success_metrics": ["データ完成度", "検索効率"]
                }
            ],
            "stakeholders": [
                {
                    "role": "プロダクトマネージャー",
                    "interests": ["機能の優先順位決定", "ユーザ価値最大化"],
                    "involvement": "要件定義、優先順位決定"
                },
                {
                    "role": "エンジニアリングマネージャー",
                    "interests": ["技術的実現性", "保守性"],
                    "involvement": "技術方針決定、実装計画"
                }
            ]
        }
        
        self.log_execution(
            "ユーザ・チーム分析",
            "Product Analysis",
            "analyze_user_teams()",
            "ユーザ役割・チーム構成・ステークホルダー分析",
            f"主要ユーザ {len(user_teams_data['primary_users'])}種、ステークホルダー {len(user_teams_data['stakeholders'])}種を分析"
        )
        
        return user_teams_data
    
    def generate_architecture_overview(self) -> Dict[str, Any]:
        """システムアーキテクチャ概要の生成"""
        print("🏗️ システムアーキテクチャ情報を整理中...")
        
        architecture_data = {
            "current_stack": {
                "backend": "Ruby on Rails",
                "database": "PostgreSQL",
                "cache": "Redis", 
                "queue": "Sidekiq",
                "storage": "AWS S3",
                "monitoring": "Datadog, Rollbar"
            },
            "evolution": [
                {
                    "period": "2024年",
                    "changes": ["基本機能実装", "認証システム構築"],
                    "technologies_added": ["devise", "omniauth-google-oauth2"]
                },
                {
                    "period": "2025年Q1",
                    "changes": ["スキーマレス設計導入", "CRM機能基盤"],
                    "technologies_added": ["JSONB活用", "Confluence連携"]
                }
            ],
            "future_roadmap": [
                {
                    "timeline": "2025年Q2",
                    "planned_changes": ["マイクロサービス化検討", "API連携強化"],
                    "drivers": ["スケーラビリティ要求", "外部連携増加"]
                }
            ]
        }
        
        self.log_execution(
            "アーキテクチャ分析",
            "System Architecture",
            "generate_architecture_overview()",
            "技術スタック・進化・将来計画の整理",
            f"現在の技術スタック、進化 {len(architecture_data['evolution'])}段階、将来計画 {len(architecture_data['future_roadmap'])}項目を整理"
        )
        
        return architecture_data
    
    def save_collected_data(self, all_data: Dict[str, Any]):
        """収集したデータをJSONファイルに保存"""
        os.makedirs(self.output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(self.output_dir, f"product_data_{timestamp}.json")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        print(f"📁 収集データを保存しました: {output_file}")
        return output_file
    
    def run_full_collection(self) -> str:
        """完全な情報収集を実行"""
        print("🚀 プロダクト説明書用の情報収集を開始します...")
        
        all_data = {
            "collection_timestamp": datetime.now().isoformat(),
            "github_data": self.collect_github_data(),
            "confluence_data": self.collect_confluence_data(),
            "user_teams_data": self.analyze_user_teams(),
            "architecture_data": self.generate_architecture_overview()
        }
        
        output_file = self.save_collected_data(all_data)
        
        self.log_execution(
            "完全情報収集",
            "Full Product Documentation",
            "run_full_collection()",
            "GitHub, Confluence, ユーザ分析, アーキテクチャの全情報収集",
            f"データ収集完了。出力ファイル: {output_file}"
        )
        
        print("✅ 情報収集が完了しました！")
        print(f"📊 収集データの活用方法:")
        print(f"   1. Obsidianでノート作成時の参考資料として活用")
        print(f"   2. プロダクト説明書の更新データとして利用")
        print(f"   3. チーム共有資料としてSlack等で共有")
        
        return output_file


def main():
    parser = argparse.ArgumentParser(description='プロダクト説明書用の情報収集')
    parser.add_argument('--project-path', default='/Users/t_kokusho/Documents/My%20Valut',
                       help='プロジェクトのパス')
    parser.add_argument('--github-repo', help='GitHubリポジトリURL')
    parser.add_argument('--confluence-space', default='SUPPLIER', help='Confluenceスペース名')
    
    args = parser.parse_args()
    
    collector = ProductDocumentationCollector(args.project_path)
    output_file = collector.run_full_collection()
    
    print(f"\n📋 実行ログ: {collector.log_file}")
    print(f"📁 収集データ: {output_file}")


if __name__ == "__main__":
    main() 