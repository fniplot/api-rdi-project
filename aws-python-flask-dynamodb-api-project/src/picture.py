import random
from src.repository import Image

class Picture:
    """画像を管理するクラス
    """    

    def __init__(self, repository) -> None:
        """初期処理

        Args:
            repository (_type_): 画像を保存するためのレポジトリ
        """
        self._repository = repository

    def create_image(self, name: str, image: str) -> Image:
        """画像情報を保存

        Args:
            name (str): 画像名
            image (str): base64 で変換した画像情報
        """        
        response = self._repository.create(name, image)
        return response

    def get_image(self, id: str) -> Image:
        """画像情報を取得

        Args:
            id (str): 画像情報に紐付く ID
        """        
        response = self._repository.get(id)
        return response

    def get_random_image(self) -> Image:
        """ランダムに画像を取得
        """        
        items = self._repository.all_get()
        ids = [item.id for item in items]
        random_ids = random.sample(ids, len(ids))
        if not random_ids:
            raise Exception("画像情報を保存されていません")

        return self._repository.get(random_ids[0])