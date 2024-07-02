import os

from dotenv import load_dotenv

from project_store import ProjectStore
from safa_client import Safa

if __name__ == '__main__':
    load_dotenv()
    VERSION_ID = os.environ["VERSION_ID"]
    USERNAME = os.environ["USERNAME"]
    PASSWORD = os.environ["PASSWORD"]
    CACHE_FILE_PATH = os.path.expanduser(os.environ["CACHE_FILE_PATH"])

    project_store = ProjectStore(CACHE_FILE_PATH)
    client = Safa(store=project_store)
    client.login(USERNAME, PASSWORD)

    project = client.get_project_data(VERSION_ID)

    # project_store.store_project("p1", project_data)
