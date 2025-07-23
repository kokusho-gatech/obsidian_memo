---
tags:
  - spec
  - supplier
  - test
  - rails
  - qa
  - guideline
---
# supplier-article テストファイル・関連リソース整理

---

## 1. コントローラーテスト（test/controllers）

### 例: users_controller_test.rb
- **テスト内容**: ユーザー管理機能（一覧、詳細、作成、更新、削除など）のコントローラ挙動
- **関連モデル**: [[User]](../../app/models/user.rb)
- **関連コントローラー**: [[UsersController]](../../app/controllers/users_controller.rb)
- **関連ビュー**: [[UsersPage]]
- **関連フィクスチャ**: [[users.yml]](../../test/fixtures/users.yml)

### 例: articles_controller_test.rb
- **テスト内容**: 物件（記事）に関する一連の操作（一覧、詳細、作成、編集、削除など）
- **関連モデル**: [[Article]](../../app/models/article.rb)
- **関連コントローラー**: [[ArticlesController]](../../app/controllers/articles_controller.rb)
- **関連ビュー**: [[ArticlesPage]]
- **関連フィクスチャ**: [[articles.yml]](../../test/fixtures/articles.yml)

### 例: intermediary_companies_controller_test.rb
- **テスト内容**: 仲介会社の管理機能
- **関連モデル**: [[IntermediaryCompany]](../../app/models/intermediary_company.rb)
- **関連コントローラー**: [[IntermediaryCompaniesController]](../../app/controllers/intermediary_companies_controller.rb)
- **関連ビュー**: [[IntermediaryCompaniesPage]]
- **関連フィクスチャ**: [[intermediary_companies.yml]](../../test/fixtures/intermediary_companies.yml)

### その他
- 各コントローラーテストファイルは、対応するコントローラー・モデル・ビュー・フィクスチャと密接に連携しています。
- サブディレクトリ（例: articles/、purchase_contracts/）配下にも詳細なテストが存在し、機能ごとに細分化されています。

---

## 2. モデルテスト（test/models）

### 例: user_test.rb
- **テスト内容**: [[User]]モデルのバリデーション、関連、メソッドの挙動
- **関連モデル**: [[User]](../../app/models/user.rb)
- **関連フィクスチャ**: [[users.yml]](../../test/fixtures/users.yml)

### 例: article_test.rb
- **テスト内容**: [[Article]]モデルのバリデーション、関連、ビジネスロジック
- **関連モデル**: [[Article]](../../app/models/article.rb)
- **関連フィクスチャ**: [[articles.yml]](../../test/fixtures/articles.yml)

### その他
- モデルごとに`*_test.rb`が存在し、バリデーションや独自メソッドの仕様を検証しています。

---

## 3. コンポーネントテスト（test/components）

### 例: table_component_test.rb
- **テスト内容**: テーブル表示用コンポーネントの描画・動作
- **関連コンポーネント**: [[TableComponent]](../../app/components/table_component.rb)（仮）
- **関連ビュー**: [[components/]](../../app/views/components/)

---

## 4. フィクスチャ（test/fixtures）

- **役割**: 各モデルのテストデータをYAML形式で定義
- **例**: [[users.yml]]、[[articles.yml]]、[[intermediary_companies.yml]] など

---

## 5. ビュー（app/views）

- **役割**: 各コントローラーのアクションに対応する画面テンプレート
- **例**: [[UsersPage]]、[[ArticlesPage]]、[[IntermediaryCompaniesPage]] など

---

## 6. まとめ

- 各テストファイルは、**対応するモデル・コントローラー・ビュー・フィクスチャ**と密接に連携し、機能ごとにテストが分割されています。
- **コントローラーテスト**は主にAPIや画面遷移の挙動、**モデルテスト**はビジネスロジックやバリデーション、**コンポーネントテスト**はUI部品の描画・動作を検証しています。
- **フィクスチャ**はテストの前提データとして活用され、仕様の一部を担っています。 