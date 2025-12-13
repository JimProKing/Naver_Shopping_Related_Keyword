import json
from pathlib import Path
from datakart import Naver
from step_1_1 import OUT_DIR

def query_naver_shop(query:str, display: int = 1) -> dict:
    NAVER_KEY = "NtYHTHvR_q16Tx29g2MT" # 비밀1
    NAVER_SEC = "3IR8ZqRJa2" # 비밀2
    naver = Naver(NAVER_KEY,NAVER_SEC)
    return naver.shop(query = query, display=display)

if __name__=="__main__":
    query="원피스"
    resp = query_naver_shop(query)
    with open(OUT_DIR / f"{Path(__file__).stem}.json","w",encoding="utf-8") as fp:
        json.dump(resp,fp,ensure_ascii=False,indent=2)