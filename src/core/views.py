from urllib.parse import urlparse

from bs4 import BeautifulSoup
from django.shortcuts import render
from django.views.generic.edit import FormView
import requests
from bottleneck.nonreduce import replace

# Create your views here.


def get_html_content(request):
    glasses = request.GET.get('glasses')
    glasses = glasses.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Windows x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    # html_content = session.get(f'https://search.shopping.naver.com/search/all?query={glasses}').text
    html_content = session.get(f'https://nsearch.wizwid.com/search/search.jsp?searchQuery={glasses}').text
    return html_content


def home(request):
    result = None

    if 'glasses' in request.GET:
        # fetch the weather from Google.
        
        html_content = get_html_content(request)
        soup = BeautifulSoup(html_content, 'html.parser')
        result = dict()
        
        res1 = soup.find("ul",{"thumbCatalog clearfix"}).select("li")
        result['res1'] = str(res1).replace(',',"").replace(']',"").replace('[',"").replace('',"")
        
        # res2 = soup.find("ul",{"class":"thumbCatalog clearfix"}).select("li > a")
        # result['res2'] = str(res2).replace(',',"").replace(']',"").replace('[',"")
        
        
        # res2 = res_href.find('')
        # res_href = soup.find("ul",{"class":"thumbCatalog clearfix"}).select('li')
        # res1 = soup.find("ul",{"class":"thumbCatalog clearfix"}).select('li > a > img')
        # result['res1'] = res1
        # result['res2'] = str(res1).replace(',',"").replace(']',"").replace('[',"")
        
        # a = list(result['res1'])
        # print(result['res1'])
        
        # str1 = " ".join(result['res1'])
        
        
        #result['res1']와 result['res2'] str임
        
        
        # b = list(result['res2'])
        #
        # c = a + b
        #
        # print(c)
        
        # result['res3'] = (a + b)
        # print(result['res3'])
        
        # print(result['res2'])
        #
        # result['res3'] = result['res1'].extend(result['res2'])
        # print(result['res3'])
        
        # str2 = " ".join(result['res2'])
        
        # result['res1'].extend(result['res2'])
        # print(result['res1'])
            
        # list_a = [a,b]
        # sum(list_a, [])
        # print(sum)
        
        # res_dict = [a+b]
        # for i, k in enumerate(a):
        #     val = b[i]
        #     res_dict[k] = val
        # def merge_dic(a, b):
        #     c = a
        #     c.update(b)
        #     return c
        # merge_dic(a, b)
        #
        #
        # print(merge_dic)
        

        
        # result['brand'] = soup.find("dd",{"class":"brand"}).text
        # result['name'] = soup.find("h4",{"class":"ellipsis multiline"}).text
        # result['price'] = soup.find("dd",{"class":"price sales"}).text
        
        
        # res1 = soup.find("ul",{"class":"thumbCatalog clearfix"})
        #
        # result['img'] = res1.find("img")["src"]
        # result['href'] = "https://www.wizwid.com/CSW/handler/wizwid/kr/MallProduct-Start?CategoryID=001115005&AssortID=707136123&ClickCategoryID="+res1.find("a")["href"]
        #
        # res2 = soup.select("ul > li > dd > dt")
        
        #
        #
        # res2 = res1.find_all('dd')
        # res2 = res1.select("ul > li > dl")
        # res3 = res2.select_one('dd')
        # result['name'] = res2.find("h4",{"class":"ellipsis multiline"}).text
        
        
        # res3 = res2.find('dl')
        # res3 = res2.find("dd")
        # result['name'] = res3.find("h4",{"class":"ellipsis multiline"}).text

        #url = 'https://search.shopping.naver.com/search/all?query=%EC%95%88%EA%B2%BD'

        #
        # html = urllib.request.urlopen(url).read()
        # context = ssl._create_unverified_context()


        # extract region
        # res1 = soup.find("ul", {"class" : "search-product-list"}).text
        # # print(res1)
        # res2 = res1.select("li > a > dl > dt > dd > div")
        # result['name'] = res2.find_one("div",{"class":"name"})


        # res1 = soup.find("ul", {"class" : "imgList_search_list__32YnP imgList_ad__1_Hus"}).text
        # res2 = res1.select("ul > li > div > div > a")
        # print(res2)


        # title_tag = soup.find('title')

        # result['price'] = soup.find("span", attrs={"class":"price_num__2WUXn"}).text
        # result['price'] = soup.find("div", attrs={"class":"_12A8D"}).text



        # res2 = res1.select_one('a')
        # res2 = res1.select("li > div > div > div")
        #
        # result['res2'] = res2.find_one("a",{"class":"imgList_link__XUg6J"}).text

        # result['price'] = res3.find("span",{"class":"price_num__2WUXn"}).text
        # result['shop'] = res3.find("span",{"class":"imgList_mall_title__3fLr4"}).text

        # res3 = soup.find("li", {"class" : "imgList_list_item__226HB"})
        # result['img'] = res3.find("img")["src"]
        # result['href'] = "https://search.shopping.naver.com/search/all?query=%EC%95%88%EA%B2%BD" + res3.find("a")["href"]
        # res4 = soup.select("li > div > imgList_list_item__226HB")
        # result['href1'] = "https://search.shopping.naver.com/search/all?query=%EC%95%88%EA%B2%BD" + res3.find("a")["href"]
        # res5 = soup.select("ul > div > imgList_list_item__226HB > img")


    return render(request, 'core/home.html', {'result': result})
