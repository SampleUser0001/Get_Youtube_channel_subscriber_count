# Get Youtube channel subscriver count

Youtubeのチャンネル登録者数を取得する。

…作ってみたが概数しか出ねえ。

## 使い方

### 準備

1. ```app/src/sample.env```をコピーして、```app/src/.env```を作成する。
2. ```app/src/.env```に環境変数を設定する。

### 実行

``` sh
docker-compose build
docker-compose run youtube_channel_subscriver_count ${チャンネルID}
```

## 参考

- [Youtubeのチャンネル登録者数を取得する:Qiita](https://qiita.com/k8uwall/items/b3a2c09d15f827fe888e)
