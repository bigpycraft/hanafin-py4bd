
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## 웹 크롤링 1/2

## 웹 페이지에서 필요한 정보 파싱
- <a href='http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'>The 50 Best Sandwiches in Chicago</a>
- 리스트 가져오기
- 각각에 연결된 가격과 주소정보 가져오기
- 가게들의 주소를 지도에 맵핑

### <font color='brown'> Beautiful Soup : 웹페이지를 읽어오는 가장 보편적인 패키지 </font>


```python
from bs4 import BeautifulSoup 
from urllib.request import urlopen
```


```python
# 구글에서 '50 Best Sandwiches' 검색
url  = 'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")
```


```python
from images import bigpycraft_bda as bpc
bpc.Figure(bpc.BDA_WC_10, 800)
```




![png](output/PE_DA_712/output_7_0.png)




```python
bpc.Figure(bpc.BDA_WC_11, 800)
```




![png](output/PE_DA_712/output_8_0.png)




```python
# 소스상세보기, Inspect로 확인
print(str(soup)[:1000])
```

    <!DOCTYPE html>
    <html lang="en">
    <head>
    <!-- Urbis magnitudo. Fabulas magnitudo. -->
    <meta charset="utf-8"/>
    <style>a.edit_from_site {display: none !important;}</style>
    <title>
      The 50 Best Sandwiches in Chicago |
      Chicago magazine
          |  November 2012
        </title>
    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable = no" name="viewport"/>
    <meta content="Our list of Chicago’s 50 best sandwiches, ranked in order of deliciousness" name="description"/>
    <!-- <meta name="description" content="Our list of Chicago’s 50 best sandwiches, ranked in order of deliciousness"> -->
    <meta content="sandwiches, dining" name="keywords"/>
    <meta content="37873197144" property="fb:pages"/>
    <link href="//www.googletagservices.com" rel="dns-prefetch"/>
    <link href="//ajax.googleapis.com" rel="dns-prefetch"/>
    <link href="//securepubads.g.doubleclick.net" rel="dns-prefetch"/>
    <link href="//media.chicagomag.com" rel="dns-prefetch"/>
    <link href="//ox-d.godengo.com/" rel="
    


```python
html_title = soup.title
html_title
```




    <title>
      The 50 Best Sandwiches in Chicago |
      Chicago magazine
          |  November 2012
        </title>




```python
tag_name = soup.title.name
tag_name
```




    'title'




```python
p_tag_name = soup.title.parent.name
p_tag_name
```




    'head'




```python
tag_text = soup.title.string
tag_text
```




    '\r\n  The 50 Best Sandwiches in Chicago |\r\n  Chicago magazine\r\n      |  November 2012\r\n    '




```python
soup.title.getText()
```




    '\r\n  The 50 Best Sandwiches in Chicago |\r\n  Chicago magazine\r\n      |  November 2012\r\n    '




```python
soup.title.get_text()
```




    '\r\n  The 50 Best Sandwiches in Chicago |\r\n  Chicago magazine\r\n      |  November 2012\r\n    '




```python
print(tag_text)
```

    
      The 50 Best Sandwiches in Chicago |
      Chicago magazine
          |  November 2012
        
    


```python
soup.div
```




    <div id="reveal-bar-mobile">
    <button id="reveal-bar-mobile-sections-button">More →</button>
    <ul class="reveal-share-buttons list-no-bullets clearfix">
    <li class="fb"><a href="https://www.facebook.com/sharer/sharer.php?u=http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/%3Futm_source=facebook.com%26utm_medium=referral%26utm_campaign=Facebook%20mobile%20reveal%20bar%2019493%20Sep%2011%202018%2012:24" onclick="ga('send',  'event', 'Sharing', 'Facebook share from mobile reveal bar','The 50 Best Sandwiches in Chicago'); return socialPopup('https://www.facebook.com/sharer/sharer.php?u=http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/%3Futm_source=facebook.com%26utm_medium=referral%26utm_campaign=Facebook%20mobile%20reveal%20bar%2019493%20Sep%2011%202018%2012:24');" target="_blank"><i class="icon-facebook"></i></a>
    </li>
    <li class="tw"><a href="https://twitter.com/share?text=The+50+Best+Sandwiches+in+Chicago&amp;url=http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/" onclick="ga('send',  'event', 'Sharing', 'Tweet story from mobile reveal bar','The 50 Best Sandwiches in Chicago'); return tweetPopup('The+50+Best+Sandwiches+in+Chicago','/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/','mobile+reveal+bar+19493');" target="_blank"><i class="icon-twitter"></i></a></li>
    </ul>
    </div>




```python
div_tags = soup.find_all('div')
```


```python
len(div_tags)
```




    217




```python
div_tags[0]
```




    <div id="reveal-bar-mobile">
    <button id="reveal-bar-mobile-sections-button">More →</button>
    <ul class="reveal-share-buttons list-no-bullets clearfix">
    <li class="fb"><a href="https://www.facebook.com/sharer/sharer.php?u=http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/%3Futm_source=facebook.com%26utm_medium=referral%26utm_campaign=Facebook%20mobile%20reveal%20bar%2019493%20Sep%2011%202018%2012:24" onclick="ga('send',  'event', 'Sharing', 'Facebook share from mobile reveal bar','The 50 Best Sandwiches in Chicago'); return socialPopup('https://www.facebook.com/sharer/sharer.php?u=http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/%3Futm_source=facebook.com%26utm_medium=referral%26utm_campaign=Facebook%20mobile%20reveal%20bar%2019493%20Sep%2011%202018%2012:24');" target="_blank"><i class="icon-facebook"></i></a>
    </li>
    <li class="tw"><a href="https://twitter.com/share?text=The+50+Best+Sandwiches+in+Chicago&amp;url=http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/" onclick="ga('send',  'event', 'Sharing', 'Tweet story from mobile reveal bar','The 50 Best Sandwiches in Chicago'); return tweetPopup('The+50+Best+Sandwiches+in+Chicago','/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/','mobile+reveal+bar+19493');" target="_blank"><i class="icon-twitter"></i></a></li>
    </ul>
    </div>




```python
type(div_tags)
```




    bs4.element.ResultSet



###  수집하고자 하는 데이터를 class명을 이용해서 구체적으로 찾아보기


```python
print(soup.find_all('div', 'sammy'))
```

    [<div class="sammy" style="position: relative;">
    <div class="sammyRank">1</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Oak-Tap-BLT/"><b>BLT</b><br/>
    Old Oak Tap<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">2</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Au-Cheval-Fried-Bologna/"><b>Fried Bologna</b><br/>
    Au Cheval<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">3</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Xoco-Woodland-Mushroom/"><b>Woodland Mushroom</b><br/>
    Xoco<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">4</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Als-Deli-Roast-Beef/"><b>Roast Beef</b><br/>
    Al’s Deli<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">5</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Publican-Quality-Meats-PB-L/"><b>PB&amp;L</b><br/>
    Publican Quality Meats<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">6</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Hendrickx-Belgian-Bread-Crafter-Belgian-Chicken-Curry-Salad/"><b>Belgian Chicken Curry Salad</b><br/>
    Hendrickx Belgian Bread Crafter<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">7</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Acadia-Lobster-Roll/"><b>Lobster Roll</b><br/>
    Acadia<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">8</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Birchwood-Kitchen-Smoked-Salmon-Salad/"><b>Smoked Salmon Salad</b><br/>
    Birchwood Kitchen<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">9</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Cemitas-Puebla-Atomica-Cemitas/"><b>Atomica Cemitas</b><br/>
    Cemitas Puebla<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">10</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Nana-Grilled-Laughing-Bird-Shrimp-and-Fried-Oyster-Po-Boy/"><b>Grilled Laughing Bird Shrimp and Fried Po’ Boy</b><br/>
    Nana<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">11</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Lula-Cafe-Ham-and-Raclette-Panino/"><b>Ham and Raclette Panino</b><br/>
    Lula Cafe<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">12</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Ricobenes-Breaded-Steak/"><b>Breaded Steak</b><br/>
    Ricobene’s<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">13</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Frog-n-Snail-The-Hawkeye/"><b>The Hawkeye</b><br/>
    Frog n Snail<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">14</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Crosbys-Kitchen-Chicken-Dip/"><b>Chicken Dip</b><br/>
    Crosby’s Kitchen<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">15</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Longman-and-Eagle-Wild-Boar-Sloppy-Joe/"><b>Wild Boar Sloppy Joe</b><br/>
    Longman &amp; Eagle<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">16</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Bari-Meatball-Sub/"><b>Meatball Sub</b><br/>
    Bari<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">17</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Mannys-Corned-Beef/"><b>Corned Beef</b><br/>
    Manny’s<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">18</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Eggys-Turkey-Club/"><b>Turkey Club</b><br/>
    Eggy’s<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">19</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Jerusalem-Falafel/"><b>Falafel</b><br/>
    Old Jerusalem<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">20</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Mindys-HotChocolate-Crab-Cake/"><b>Crab Cake</b><br/>
    Mindy’s HotChocolate<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">21</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Olgas-Delicatessen-Chicken-Schnitzel/"><b>Chicken Schnitzel</b><br/>
    Olga’s Delicatessen<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">22</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Dawali-Mediterranean-Kitchen-Shawarma/"><b>Shawarma</b><br/>
    Dawali Mediterranean Kitchen<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">23</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Big-Jones-Toasted-Pimiento-Cheese/"><b>Toasted Pimiento Cheese</b><br/>
    Big Jones<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">24</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-La-Pane-Vegetarian-Panino/"><b>Vegetarian Panino</b><br/>
    La Pane<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">25</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Pastoral-Cali-Chevre/"><b>Cali Chèvre</b><br/>
    Pastoral<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">26</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Maxs-Deli-Pastrami/"><b>Pastrami</b><br/>
    Max’s Deli<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">27</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Luckys-Sandwich-Co-The-Fredo/"><b>The Fredo</b><br/>
    Lucky’s Sandwich Co.<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">28</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-City-Provisions-Smoked-Ham/"><b>Smoked Ham</b><br/>
    City Provisions<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">29</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Papas-Cache-Sabroso-Jibarito/"><b>Jibarito</b><br/>
    Papa’s Cache Sabroso<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">30</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Bavettes-Bar-and-Boeuf-Shaved-Prime-Rib/"><b>Shaved Prime Rib</b><br/>
    Bavette’s Bar &amp; Boeuf<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">31</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Hannahs-Bretzel-Serrano-Ham-and-Manchego-Cheese/"><b>Serrano Ham and Manchego Cheese</b><br/>
    Hannah’s Bretzel<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">32</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-La-Fournette-Tuna-Salad/"><b>Tuna Salad</b><br/>
    La Fournette<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">33</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Paramount-Room-Paramount-Reuben/"><b>Paramount Reuben</b><br/>
    Paramount Room<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">34</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Melt-Sandwich-Shoppe-The-Istanbul/"><b>The Istanbul</b><br/>
    Melt Sandwich Shoppe<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">35</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Floriole-Cafe-and-Bakery-BAD/"><b>B.A.D.</b><br/>
    Floriole Cafe &amp; Bakery<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">36</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-First-Slice-Pie-Cafe-Duck-Confit-and-Mozzarella/"><b>Duck Confit and Mozzarella</b><br/>
    First Slice Pie Café<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">37</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Troquet-Croque-Monsieur/"><b>Croque Monsieur</b><br/>
    Troquet<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">38</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Grahamwich-Green-Garbanzo/"><b>Green Garbanzo</b><br/>
    Grahamwich<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">39</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Saigon-Sisters-The-Hen-House/"><b>The Hen House</b><br/>
    Saigon Sisters<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">40</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Rosalias-Deli-Tuscan-Chicken/"><b>Tuscan Chicken</b><br/>
    Rosalia’s Deli<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">41</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Z-and-H-MarketCafe-The-Marty/"><b>The Marty </b><br/>
    Z&amp;H MarketCafe<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">42</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Market-House-on-the-Square-Whitefish/"><b>Whitefish</b><br/>
    Market House on the Square<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">43</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Elaines-Coffee-Call-Oat-Bread-Pecan-Butter-and-Fruit-Jam/"><b>Oat Bread, Pecan Butter, and Fruit Jam</b><br/>
    Elaine’s Coffee Call<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">44</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Marion-Street-Cheese-Market-Cauliflower-Melt/"><b>Cauliflower Melt</b><br/>
    Marion Street Cheese Market<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">45</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Cafecito-Cubano/"><b>Cubana</b><br/>
    Cafecito<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">46</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Chickpea-Kufta/"><b>Kufta</b><br/>
    Chickpea<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">47</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-The-Goddess-and-Grocer-Debbies-Egg-Salad/"><b>Debbie’s Egg Salad</b><br/>
    The Goddess and Grocer<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">48</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Zenwich-Beef-Curry/"><b>Beef Curry</b><br/>
    Zenwich<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative;">
    <div class="sammyRank">49</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Toni-Patisserie-Le-Vegetarien/"><b>Le Végétarien</b><br/>
    Toni Patisserie<br/>
    <em>Read more</em> </a></div>
    </div>, <div class="sammy" style="position: relative; border-bottom: 0">
    <div class="sammyRank">50</div>
    <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Phoebes-Bakery-The-Gatsby/"><b>The Gatsby</b><br/>
    Phoebe’s Bakery<br/>
    <em>Read more</em> </a></div>
    </div>]
    


```python
len(soup.find_all('div', 'sammy'))
```




    50




```python
print(soup.find_all('div', 'sammyListing'))
```

    [<div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Oak-Tap-BLT/"><b>BLT</b><br/>
    Old Oak Tap<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Au-Cheval-Fried-Bologna/"><b>Fried Bologna</b><br/>
    Au Cheval<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Xoco-Woodland-Mushroom/"><b>Woodland Mushroom</b><br/>
    Xoco<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Als-Deli-Roast-Beef/"><b>Roast Beef</b><br/>
    Al’s Deli<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Publican-Quality-Meats-PB-L/"><b>PB&amp;L</b><br/>
    Publican Quality Meats<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Hendrickx-Belgian-Bread-Crafter-Belgian-Chicken-Curry-Salad/"><b>Belgian Chicken Curry Salad</b><br/>
    Hendrickx Belgian Bread Crafter<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Acadia-Lobster-Roll/"><b>Lobster Roll</b><br/>
    Acadia<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Birchwood-Kitchen-Smoked-Salmon-Salad/"><b>Smoked Salmon Salad</b><br/>
    Birchwood Kitchen<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Cemitas-Puebla-Atomica-Cemitas/"><b>Atomica Cemitas</b><br/>
    Cemitas Puebla<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Nana-Grilled-Laughing-Bird-Shrimp-and-Fried-Oyster-Po-Boy/"><b>Grilled Laughing Bird Shrimp and Fried Po’ Boy</b><br/>
    Nana<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Lula-Cafe-Ham-and-Raclette-Panino/"><b>Ham and Raclette Panino</b><br/>
    Lula Cafe<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Ricobenes-Breaded-Steak/"><b>Breaded Steak</b><br/>
    Ricobene’s<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Frog-n-Snail-The-Hawkeye/"><b>The Hawkeye</b><br/>
    Frog n Snail<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Crosbys-Kitchen-Chicken-Dip/"><b>Chicken Dip</b><br/>
    Crosby’s Kitchen<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Longman-and-Eagle-Wild-Boar-Sloppy-Joe/"><b>Wild Boar Sloppy Joe</b><br/>
    Longman &amp; Eagle<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Bari-Meatball-Sub/"><b>Meatball Sub</b><br/>
    Bari<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Mannys-Corned-Beef/"><b>Corned Beef</b><br/>
    Manny’s<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Eggys-Turkey-Club/"><b>Turkey Club</b><br/>
    Eggy’s<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Jerusalem-Falafel/"><b>Falafel</b><br/>
    Old Jerusalem<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Mindys-HotChocolate-Crab-Cake/"><b>Crab Cake</b><br/>
    Mindy’s HotChocolate<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Olgas-Delicatessen-Chicken-Schnitzel/"><b>Chicken Schnitzel</b><br/>
    Olga’s Delicatessen<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Dawali-Mediterranean-Kitchen-Shawarma/"><b>Shawarma</b><br/>
    Dawali Mediterranean Kitchen<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Big-Jones-Toasted-Pimiento-Cheese/"><b>Toasted Pimiento Cheese</b><br/>
    Big Jones<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-La-Pane-Vegetarian-Panino/"><b>Vegetarian Panino</b><br/>
    La Pane<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Pastoral-Cali-Chevre/"><b>Cali Chèvre</b><br/>
    Pastoral<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Maxs-Deli-Pastrami/"><b>Pastrami</b><br/>
    Max’s Deli<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Luckys-Sandwich-Co-The-Fredo/"><b>The Fredo</b><br/>
    Lucky’s Sandwich Co.<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-City-Provisions-Smoked-Ham/"><b>Smoked Ham</b><br/>
    City Provisions<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Papas-Cache-Sabroso-Jibarito/"><b>Jibarito</b><br/>
    Papa’s Cache Sabroso<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Bavettes-Bar-and-Boeuf-Shaved-Prime-Rib/"><b>Shaved Prime Rib</b><br/>
    Bavette’s Bar &amp; Boeuf<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Hannahs-Bretzel-Serrano-Ham-and-Manchego-Cheese/"><b>Serrano Ham and Manchego Cheese</b><br/>
    Hannah’s Bretzel<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-La-Fournette-Tuna-Salad/"><b>Tuna Salad</b><br/>
    La Fournette<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Paramount-Room-Paramount-Reuben/"><b>Paramount Reuben</b><br/>
    Paramount Room<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Melt-Sandwich-Shoppe-The-Istanbul/"><b>The Istanbul</b><br/>
    Melt Sandwich Shoppe<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Floriole-Cafe-and-Bakery-BAD/"><b>B.A.D.</b><br/>
    Floriole Cafe &amp; Bakery<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-First-Slice-Pie-Cafe-Duck-Confit-and-Mozzarella/"><b>Duck Confit and Mozzarella</b><br/>
    First Slice Pie Café<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Troquet-Croque-Monsieur/"><b>Croque Monsieur</b><br/>
    Troquet<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Grahamwich-Green-Garbanzo/"><b>Green Garbanzo</b><br/>
    Grahamwich<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Saigon-Sisters-The-Hen-House/"><b>The Hen House</b><br/>
    Saigon Sisters<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Rosalias-Deli-Tuscan-Chicken/"><b>Tuscan Chicken</b><br/>
    Rosalia’s Deli<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Z-and-H-MarketCafe-The-Marty/"><b>The Marty </b><br/>
    Z&amp;H MarketCafe<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Market-House-on-the-Square-Whitefish/"><b>Whitefish</b><br/>
    Market House on the Square<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Elaines-Coffee-Call-Oat-Bread-Pecan-Butter-and-Fruit-Jam/"><b>Oat Bread, Pecan Butter, and Fruit Jam</b><br/>
    Elaine’s Coffee Call<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Marion-Street-Cheese-Market-Cauliflower-Melt/"><b>Cauliflower Melt</b><br/>
    Marion Street Cheese Market<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Cafecito-Cubano/"><b>Cubana</b><br/>
    Cafecito<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Chickpea-Kufta/"><b>Kufta</b><br/>
    Chickpea<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-The-Goddess-and-Grocer-Debbies-Egg-Salad/"><b>Debbie’s Egg Salad</b><br/>
    The Goddess and Grocer<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Zenwich-Beef-Curry/"><b>Beef Curry</b><br/>
    Zenwich<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Toni-Patisserie-Le-Vegetarien/"><b>Le Végétarien</b><br/>
    Toni Patisserie<br/>
    <em>Read more</em> </a></div>, <div class="sammyListing"><a href="http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Phoebes-Bakery-The-Gatsby/"><b>The Gatsby</b><br/>
    Phoebe’s Bakery<br/>
    <em>Read more</em> </a></div>]
    


```python
print(soup.find_all('div', 'sammyRank'))
```

    [<div class="sammyRank">1</div>, <div class="sammyRank">2</div>, <div class="sammyRank">3</div>, <div class="sammyRank">4</div>, <div class="sammyRank">5</div>, <div class="sammyRank">6</div>, <div class="sammyRank">7</div>, <div class="sammyRank">8</div>, <div class="sammyRank">9</div>, <div class="sammyRank">10</div>, <div class="sammyRank">11</div>, <div class="sammyRank">12</div>, <div class="sammyRank">13</div>, <div class="sammyRank">14</div>, <div class="sammyRank">15</div>, <div class="sammyRank">16</div>, <div class="sammyRank">17</div>, <div class="sammyRank">18</div>, <div class="sammyRank">19</div>, <div class="sammyRank">20</div>, <div class="sammyRank">21</div>, <div class="sammyRank">22</div>, <div class="sammyRank">23</div>, <div class="sammyRank">24</div>, <div class="sammyRank">25</div>, <div class="sammyRank">26</div>, <div class="sammyRank">27</div>, <div class="sammyRank">28</div>, <div class="sammyRank">29</div>, <div class="sammyRank">30</div>, <div class="sammyRank">31</div>, <div class="sammyRank">32</div>, <div class="sammyRank">33</div>, <div class="sammyRank">34</div>, <div class="sammyRank">35</div>, <div class="sammyRank">36</div>, <div class="sammyRank">37</div>, <div class="sammyRank">38</div>, <div class="sammyRank">39</div>, <div class="sammyRank">40</div>, <div class="sammyRank">41</div>, <div class="sammyRank">42</div>, <div class="sammyRank">43</div>, <div class="sammyRank">44</div>, <div class="sammyRank">45</div>, <div class="sammyRank">46</div>, <div class="sammyRank">47</div>, <div class="sammyRank">48</div>, <div class="sammyRank">49</div>, <div class="sammyRank">50</div>]
    


```python
tmp = soup.find_all('div', 'sammyRank')
tmp[0].get_text()
```




    '1'




```python
listOfsoup = soup.find_all('div', 'sammy')
listOfsoup[0]
```




    <div class="sammy" style="position: relative;">
    <div class="sammyRank">1</div>
    <div class="sammyListing"><a href="/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Oak-Tap-BLT/"><b>BLT</b><br/>
    Old Oak Tap<br/>
    <em>Read more</em> </a></div>
    </div>




```python
rank = []

for item in listOfsoup:
    rank.append(item.find('div', 'sammyRank').get_text())
    
rank[:10]
```




    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']




```python
listOfsoup[0].find("a").get_text()
```




    'BLT\r\nOld Oak Tap\nRead more '




```python
listOfsoup[0].find("a")['href']
```




    '/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Oak-Tap-BLT/'



### <font color='brown'> 정규식 : Regular Expresion 모듈 </font>


```python
import re
```


```python
tmpString = str(listOfsoup[0].find("a").get_text())
tmpString
```




    'BLT\r\nOld Oak Tap\nRead more '



#### <font color='blue'> # \n or \r\n 으로 들어가는 부분을 구분 </font>


```python
re.split(('\n|\r\n'), tmpString)
```




    ['BLT', 'Old Oak Tap', 'Read more ']




```python
re.split(('\n|\r\n'), tmpString)[0]
```




    'BLT'




```python
re.split(('\n|\r\n'), tmpString)[1]
```




    'Old Oak Tap'




```python
listOfsoup[10].find("a")["href"]
```




    'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Lula-Cafe-Ham-and-Raclette-Panino/'




```python
rank = []

mainMenu = []
cafeName = []
urlAdd   = []

for item in listOfsoup:
    rank.append(item.find('div', 'sammyRank').get_text())
    
    tmpString = str(item.find("a").get_text())
    mainMenu.append(re.split(('\n|\r\n'), tmpString)[0])
    cafeName.append(re.split(('\n|\r\n'), tmpString)[1])
    
    urlAdd.append(item.find("a")["href"])
```


```python
rank[:5]
```




    ['1', '2', '3', '4', '5']




```python
mainMenu[:5]
```




    ['BLT', 'Fried Bologna', 'Woodland Mushroom', 'Roast Beef', 'PB&L']




```python
cafeName[:5]
```




    ['Old Oak Tap', 'Au Cheval', 'Xoco', 'Al’s Deli', 'Publican Quality Meats']




```python
urlAdd[:10]
```




    ['/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Oak-Tap-BLT/',
     '/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Au-Cheval-Fried-Bologna/',
     '/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Xoco-Woodland-Mushroom/',
     '/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Als-Deli-Roast-Beef/',
     '/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Publican-Quality-Meats-PB-L/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Hendrickx-Belgian-Bread-Crafter-Belgian-Chicken-Curry-Salad/',
     '/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Acadia-Lobster-Roll/',
     '/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Birchwood-Kitchen-Smoked-Salmon-Salad/',
     '/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Cemitas-Puebla-Atomica-Cemitas/',
     '/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Nana-Grilled-Laughing-Bird-Shrimp-and-Fried-Oyster-Po-Boy/']




```python
urlAdd[5][:4]
```




    'http'




```python
rank = []

mainMenu = []
cafeName = []
urlAdd   = []

for item in listOfsoup:
    rank.append(item.find('div', 'sammyRank').get_text())
    
    tmpString = str(item.find("a").get_text())
    tmp = [tmpLine for tmpLine in re.split(('\n|\r\n'), tmpString)]
    mainMenu.append(tmp[0])
    cafeName.append(tmp[1])
    
    tmp2 = item.find("a")["href"]
    if tmp2[:4] != 'http':
        urlAdd.append('http://www.chicagomag.com'+item.find("a")["href"])
    else :
        urlAdd.append(item.find("a")["href"])
```


```python
urlAdd[:10]
```




    ['http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Oak-Tap-BLT/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Au-Cheval-Fried-Bologna/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Xoco-Woodland-Mushroom/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Als-Deli-Roast-Beef/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Publican-Quality-Meats-PB-L/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Hendrickx-Belgian-Bread-Crafter-Belgian-Chicken-Curry-Salad/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Acadia-Lobster-Roll/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Birchwood-Kitchen-Smoked-Salmon-Salad/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Cemitas-Puebla-Atomica-Cemitas/',
     'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Nana-Grilled-Laughing-Bird-Shrimp-and-Fried-Oyster-Po-Boy/']



#### <font color='blue'> # 가져온 데이터를 데이터프레임으로 정라한 후,  파일로 저장하기 </font>


```python
import pandas as pd

data = {'Rank':rank, 'Menu':mainMenu, 'Cafe':cafeName, 'URL':urlAdd}
df = pd.DataFrame(data)
```


```python
df.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cafe</th>
      <th>Menu</th>
      <th>Rank</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>1</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>2</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>3</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>4</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>5</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hendrickx Belgian Bread Crafter</td>
      <td>Belgian Chicken Curry Salad</td>
      <td>6</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Acadia</td>
      <td>Lobster Roll</td>
      <td>7</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Birchwood Kitchen</td>
      <td>Smoked Salmon Salad</td>
      <td>8</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Cemitas Puebla</td>
      <td>Atomica Cemitas</td>
      <td>9</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Nana</td>
      <td>Grilled Laughing Bird Shrimp and Fried Po’ Boy</td>
      <td>10</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
  </tbody>
</table>
</div>



#### <font color='blue'> # 컬럼 순서 조정하기 </font>


```python
df = pd.DataFrame(data, columns=['Rank','Cafe','Menu','URL'])
df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Cafe</th>
      <th>Menu</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
  </tbody>
</table>
</div>



#### <font color='blue'> # 웹파싱한 데이터 파일로 저장하기 </font>


```python
df.to_csv('data/chicagomag_info.csv', sep=',', encoding='UTF-8')
```


```python
# % ls data
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
