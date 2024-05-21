import dataclasses
import uuid

def search_key(id: str, name: str=None, image: str=None):
    """データを検索するデータ構造を生成

    Args:
        id (str): 画像 ID
        name (str, optional): 画像名 デフォルト値は None
        image (str, optional): 画像イメージ デフォルト値は None

    Returns:
        object: 検索するデータ構造を返却。
    Toto:
        返却するデータ構造例：
            {'id': {'S': 1}, 'name': {'S': 'name'}, 'image': {'S': 'image'}}
    """    
    search = {
        'id': 'S',
        'name': 'S',
        'image': 'S'
    }
    return {
        key: {
            search[key]: value
        } for key, value in zip(search.keys(), [id, name, image]) if value
    }

@dataclasses.dataclass
class Image:
    """画像情報のデータクラス
    """    
    id: str # 画像 ID
    name: str # 画像名
    image: str # 画像イメージ

class Repository:
    """DynamoDB を操作するレポジトリクラス
    """
    def __init__(self, client: object, table_name: str) -> None:
        """初期処理

        Args:
            client (object): DB のオブジェクト
            table_name (str): テーブル名
        """        
        self._client = client
        self._table_name = table_name

    def get(self, id: str) -> Image:
        """詳細な画像情報を取得

        Args:
            id (str): 画像 ID

        Returns:
            Image: 画像情報を返す
        """        
        item = self._client.get_item(
            TableName=self._table_name, 
            Key=search_key(id)
        )

        if item.get('Item') is None and item['ResponseMetadata']['HTTPStatusCode'] == 200:
            return Image('', '', '')
        elif item.get('Item') is not None and item['ResponseMetadata']['HTTPStatusCode'] == 200:
            return Image(
                item.get('Item').get('id').get('S'),
                item.get('Item').get('name').get('S'),
                item.get('Item').get('image').get('S')
            )
        else:
            pass

    def create(self, name: str, image: str) -> Image:
        """画像情報を登録

        Args:
            name (str): 画像名
            image (str): 画像イメージ
        """        
        id = str(uuid.uuid4()).replace('-', '')
        self._client.put_item(
            TableName=self._table_name, 
            Item=search_key(id, name, image)
        )

        return Image(id, name, image)

    def all_get(self) -> list:
        """すべての画像情報を取得
        """        
        images = []
        items = self._client.scan(TableName=self._table_name).get('Items', [])
        for item in items:
            images.append(Image(
                item.get('id').get('S'),
                item.get('name').get('S'),
                item.get('image').get('S')
            ))
        return images
