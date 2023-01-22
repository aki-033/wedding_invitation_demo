# 結婚式WEB招待状 with Django (DEMO版)

## これはなに？

### Djangoで作った結婚式用WEB招待状(DEMO)

これはDjangoによる結婚式WEB招待状システムの**DEMO版**です。

2022/10/08に開催された結婚式にて実際に使用されました。(本番環境はHerokuを使用)

### トップページ

![Readme Image 1](readme_img/wi_readme_1.jpg)

### 回答フォーム

![Readme Image 1](readme_img/wi_readme_2.jpg)





## 開発環境でのシステムの起動方法

1. settings_local_sample.pyをもとに**settings_local.py**を作成し、settings.pyと同階層に配置する。
2. DBのマイグレーションを行う。
3. 管理者アカウントを作製する。
4. Djangoのサーバーを起動する。`python manage.py runserver`
5. 招待客のアカウントを作製する(このときユーザー名はUUIDにて作製する。)


## 招待客への招待状の通知

### 招待客用のリンクの作製

招待客毎にユーザー名から招待用リンクを作製する。

招待客のユーザー名をクエリ「guest」としてログインURLを作製する。ユーザー名が「C8E91020-7CCD-4364-AB54-3BDE08597C4F」の場合、以下のようになる。

http://example.com/login/?guest=C8E91020-7CCD-4364-AB54-3BDE08597C4F

### リンクの通知

このURLとユーザーパスワードをメッセージアプリやメール等で対象の招待客に通知する。招待客がこのURLにアクセスすることでログインページが表示される。

## VPS(AWS)環境へのデプロイ方法

manage.pyと同階層に.envファイルを作成し以下の項目を記述する。

```
SECRET_KEY=(例)piyopiyo
DEBUG=False
DATABASE_URL=(例)postgres://djangopg:hogehoge@localhost:/djangopgdb
```

**settings_local.pyは作成しない。**