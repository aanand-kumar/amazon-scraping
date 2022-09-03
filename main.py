
import requests
from bs4 import BeautifulSoup
import lxml
url = "https://www.amazon.in/Sparx-SFG-204-Beige-Brown-SF0204G_BRBD_0006/dp/B09Q5DG8RS/ref=pd_rhf_d_dp_s_pd_crcbs_sccl_2_7/260-8213024-3258244?pd_rd_w=laP9r&content-id=amzn1.sym.5d8cdd8d-be53-4391-b82d-376d461d85f0&pf_rd_p=5d8cdd8d-be53-4391-b82d-376d461d85f0&pf_rd_r=2W6W6E6E697H9R31G4SC&pd_rd_wg=gdgmI&pd_rd_r=69ae1484-0313-450e-b893-a1e8cf7a3274&pd_rd_i=B0BC99KSD7&psc=1"


url2= "https://www.amazon.in/gp/product/B08ZJQWWTN/ref=s9_acss_bw_cg_Budget_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-16&pf_rd_r=QD324D0299HMJCMGVEKZ&pf_rd_t=101&pf_rd_p=8b04d26d-599b-4893-b1c8-fae62e9b9b89&pf_rd_i=1389401031&th=1"

url3 = "https://www.amazon.in/Sennheiser-CX-80s-Ear-Earphone/dp/B083T5G5PM/ref=sr_1_4?keywords=sennheiser&qid=1662200918&s=electronics&sr=1-4"

def convert_float(s):
  s= s.replace(',', '')
  return float(s)

def get_link_data(url):
  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36     (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en",
  }
  r = requests.get(url, headers=headers) 
  soup = BeautifulSoup(r.text, "lxml")

  name = soup.select_one(selector="#productTitle").getText()
  name = name.strip()  
  price = soup.select_one(selector=".a-price >.a-offscreen").getText()
  price = convert_float(price[1:])
  return name, price


print(get_link_data(url3))