
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## 웹 크롤링 심화

### 맥도날드 지수 구하기 
- 사이트 : http://www.mcdonalds.co.kr/www/kor/findus/district.do
- 맥도날드 사이트에서 서울 지역의 매장검색
- 서울시 지도에 매장 분포도 작성
- 맥도널드는 어디에 가장 많은 매장을 가지고 있을까??


```python
from itertools import count
from tqdm import tqdm_notebook
from time import sleep
from bs4 import BeautifulSoup 
from urllib.request import urlopen

import pandas as pd
```


```python

# bpc.Figure(bpc.BDA_WC_20, 1000)
```




![png](output_5_0.png)




```python
html = 'http://www.mcdonalds.co.kr/www/kor/findus/district.do?pageIndex={page}&sSearch_yn=Y&skey=2&skey1=&skey2=&skeyword=%EC%84%9C%EC%9A%B8&skey4=&skey5=&skeyword2=&sflag1=&sflag2=&sflag3=&sflag4=&sflag5=&sflag6=&sflag=N'

response = urlopen(html.format(page=1))

soup = BeautifulSoup(response, "lxml")
soup
```




    <!DOCTYPE html>
    <html lang="ko">
    <head>
    <meta charset="utf-8"/>
    <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
    <meta content="소시지맥머핀, 듀엣세트, 맥도날드듀엣세트, 소세지맥머핀, 맥머핀, 에그맥머핀, 베이컨에그맥머핀, 소시지에그맥머핀, 아침배달음식, 브런치배달, 아침밥배달, 아침식사, 주말아침, 주말아침식사, 맥모닝, 맥딜리버리, 간단한아침식사, 간단한아침식사배달, 아침도시락배달, 아침배달, 아침식사배달, 아침식사배달업체, 주말간단한아침메뉴, 주말아침배달, 주말아침식사배달, 브런치메뉴, 브런치추천, 아침, 아침식사메뉴, 아침메뉴, 간단한아침메뉴, 아침대용식, 빅브렉퍼스트" name="description"/>
    <title>지역별 - McDonald's</title>
    <link href="/www/common/images/favicon.ico" rel="shortcut icon"/>
    <link href="../../common/css/normalize.css" rel="stylesheet" type="text/css"/>
    <link href="../../common/css/common.css" rel="stylesheet" type="text/css"/>
    <link href="../../common/css/sub.css" rel="stylesheet" type="text/css"/>
    <script src="../../common/js_ui/lib/jquery-1.10.2.min.js" type="text/javascript"></script>
    <script src="../../common/js_ui/lib/jquery.textPlaceholder.js" type="text/javascript"></script>
    <script src="../../common/js_ui/lib/html5shiv-printshiv.js" type="text/javascript"></script>
    <script src="../../common/js_ui/mcd_ui.js" type="text/javascript"></script>
    <script type="text/javascript">
    	var mobileKeyWords = new Array('iPhone', 'iPod', 'BlackBerry', 'Android', 'Windows CE', 'LG', 'MOT', 'SAMSUNG', 'SonyEricsson');
    	for (var word in mobileKeyWords){
    		if (navigator.userAgent.match(mobileKeyWords[word]) != null){
    			location.href = "http://m.mcdonalds.co.kr/me/kor/findus/district.do";
    		break;
    		}
     	}
    </script>
    <!--[if lt IE 9]>
        <script type="text/javascript">
            document.createElement("header"); document.createElement("nav"); document.createElement("section"); document.createElement("article"); document.createElement("footer");
        </script>
    <![endif]-->
    <script>
    function shGugunAjax(sobj,tobj,tagid){
    
        $.ajax({
            url : "/www/kor/ajax/ajax.usr_gugun.do",
            type : "POST",
            data : {"sido" : $("#"+sobj).val() , "tagid" : tagid} ,
            dataType : "text",
            success : function(response) {
                if(response != "") {
                    $("#"+tobj).html(response);
                    return;
                }
            },
            error : function(request, status, error) {
                if (request.status != '0') {
                    alert("code : " + request.status + "\r\nmessage : "
                        + request.reponseText + "\r\nerror : " + error);
                }
            }
        });
    }
    </script>
    <script charset="utf-8" src="http://apis.daum.net/maps/maps3.js?apikey=dd4031904c7964687d86513ffbcad30cb714e287" type="text/javascript"></script>
    <script type="text/javascript">
        var map;
        window.onload = function () {
    
            var latitude = "";
            var longitude = "";
    
            
                
                    
                            
                                
                                    latitude = 37.494879;
                                    longitude = 127.130762;
                                
                            
                    
                            
                                
                            
                    
                            
                                
                            
                    
                            
                                
                            
                    
                            
                                
                            
                    
                
                
            
    
            map = new daum.maps.Map(document.getElementById('map'), {
                center: new daum.maps.LatLng(latitude,longitude),
                level: 7
            });
    
            var points = [
                
                    
                        
                                
                                    
                                        new daum.maps.LatLng(37.494879,127.130762)
                                    
                                    
                                
                        
                                
                                    
                                    
                                        ,new daum.maps.LatLng(37.4813244,126.8837789)
                                    
                                
                        
                                
                                    
                                    
                                        ,new daum.maps.LatLng(37.4801705,126.8811402)
                                    
                                
                        
                                
                                    
                                    
                                        ,new daum.maps.LatLng(37.4986859,127.0287553)
                                    
                                
                        
                                
                                    
                                    
                                        ,new daum.maps.LatLng(37.5162358,127.0413134)
                                    
                                
                        
                    
                
            ];
            var icon = [
                
                    
                        
                                
                                    
                                    new daum.maps.MarkerImage( '/www/common/images/kor/store/maker'+1+'.png', new daum.maps.Size(35, 32)  )
    
                                    
                                    
                                
                        
                                
                                    
                                    
                                        ,new daum.maps.MarkerImage( '/www/common/images/kor/store/maker'+2+'.png', new daum.maps.Size(35, 32)  )
                                    
                                
                        
                                
                                    
                                    
                                        ,new daum.maps.MarkerImage( '/www/common/images/kor/store/maker'+3+'.png', new daum.maps.Size(35, 32)  )
                                    
                                
                        
                                
                                    
                                    
                                        ,new daum.maps.MarkerImage( '/www/common/images/kor/store/maker'+4+'.png', new daum.maps.Size(35, 32)  )
                                    
                                
                        
                                
                                    
                                    
                                        ,new daum.maps.MarkerImage( '/www/common/images/kor/store/maker'+5+'.png', new daum.maps.Size(35, 32)  )
                                    
                                
                        
                    
                
            ];
    
            //######## Zooming, 지도/스카이 뷰 start ########
            var zoomControl = new daum.maps.ZoomControl();
            map.addControl(zoomControl, daum.maps.ControlPosition.RIGHT);
            var mapTypeControl = new daum.maps.MapTypeControl();
            map.addControl(mapTypeControl, daum.maps.ControlPosition.TOPRIGHT);
            //######## Zooming, 지도/스카이 뷰 End ########
    
    
            for(var i = 0; i < points.length; i++){
                new daum.maps.Marker({
                    position: points[i],
                    image: icon[i]
                }).setMap(map);
            }
        }
    
        function EnterSubmitLocal() {
            if(event.keyCode == 13) {
                shSubmit();
            }
        }
    
        function shSubmit(){
            document.shForm.submit();
        }
    
        function printBtn(){
            print();
        }
    
        function shSubmit(){
            var form = document.shForm;
            if ($("#skeyword").val() == "") {
    			alert("매장명, 동명, 도로명을 입력하세요");
    			$("#skeyword").focus();
    			return;
    		} else {
    			form.submit();
    	        return;
    		}
        }
    
        function moveMap(xx,yy){
            var po = new daum.maps.LatLng(xx, yy);
            map.setCenter(po);
        }
    
        function radioCheck(_gubun) {
            if (_gubun == "1") {
    			$("#skey4 option:eq(0)").attr("selected", "selected");
    			var opt2 = $("#skey5 option").size();
    			for(var i=1;i<opt2;i++)
    			{
    				$("#skey5 option:last").remove();
    			}
                $("#skeyword1").val("");
                $("#skeyword").val("");
                $("#skeyword2").val("");
            } else if(_gubun == "2"){
    			$("#skey1 option:eq(0)").attr("selected", "selected");
    			$("#skey4 option:eq(0)").attr("selected", "selected");
    			var opt1 = $("#skey2 option").size();
    			for(var i=1;i<opt1;i++)
    			{
    				$("#skey2 option:last").remove();
    			}
    			var opt2 = $("#skey5 option").size();
    			for(var i=1;i<opt2;i++)
    			{
    				$("#skey5 option:last").remove();
    			}
                $("#skeyword1").val("");
                $("#skeyword2").val("");
            } else if(_gubun == "3"){
    			$("#skey1 option:eq(0)").attr("selected", "selected");
    			var opt1 = $("#skey2 option").size();
    			for(var i=1;i<opt1;i++)
    			{
    				$("#skey2 option:last").remove();
    			}
                $("#skeyword").val("");
                $("#skeyword1").val("");
            }
            $('input:radio[name="skey"]:input[value="' + _gubun + '"]').prop("checked", true);
        }
    </script>
    <style>
    .searchResult ul.listHeader li{width:auto;padding:0 15px 13px}
    .searchResult ul.listHeader li:first-child{width:200px;}
    .searchResult ul.listHeader li:last-child{padding-right:0}
    .searchResult ul.resultList li div.detail{padding:0 0 0 10px}
    .searchResult ul.resultList li dl dd{width:178px;padding-left:20px;line-height:19px;letter-spacing:-0.3px;text-align:justify}
    .searchResult ul.resultList li dl dd.infoCheck span{vertical-align:top}
    .searchResult ul.resultList li dl dd.infoCheck{width:572px}
    span.except {display: block !important;clear: both;width:59px !important;color: #ae0b0c;margin:0 auto}
    </style>
    </head>
    <body class="findusBg">
    <!-- WIDERPLANET  SCRIPT START 2015.4.17 -->
    <div id="wp_tg_cts" style="display:none;"></div>
    <script type="text/javascript">
    var wptg_tagscript_vars = wptg_tagscript_vars || [];
    wptg_tagscript_vars.push(
    (function() {
    return {
               ti:"21843",         /*광고주 코드*/
               ty:"Home",         /*트래킹태그 타입*/
               device:"web"      /*디바이스 종류 (web 또는 mobile)*/
    };
    }));
    </script>
    <script async="" src="//astg.widerplanet.com/js/wp_astg_3.0.js" type="text/javascript"></script>
    <!-- // WIDERPLANET  SCRIPT END 2015.4.17 -->
    <div class="skipNavigation">
    <a href="#contents">본문바로가기</a>
    <a href="#gnb">글로벌 네비게이션</a>
    <a href="#footer">하단영역</a>
    </div>
    <div id="wrap"><!-- wrap -->
    <header id="header"><!-- Header -->
    <h1><a href="/www/kor/main/main.do"><img alt="I’m lovin’ it" height="95" src="/www/common/images/kor/common/header/logo.png" width="105"/></a></h1>
    <script>
            function EnterSubmit() {
                if(event.keyCode == 13) {
                    leftShSubmit();
                }
            }
            function EnterSubmit1() {
                if(event.keyCode == 13) {
                    leftShSubmit1();
                }
            }
            function leftShSubmit(){
                var form = document.leftShForm;
                if (form.sLeftKeyword1.value == "" )	{
                    alert("키워드를 입력해 주세요.");
                    form.sLeftKeyword1.focus();
                    return;
                }
                //form.action = "/www/kor/findus/district.do?sSearch_yn=Y&skey=2&skeyword="+document.leftShForm.sLeftKeyword1.value;
                form.setAttribute('action','/www/kor/findus/district.do?sSearch_yn=Y&skey=2&skeyword='+form.sLeftKeyword1.value);
                form.submit();
            }
            function leftShSubmit1(){
                var form = document.leftShForm1;
                if (document.leftShForm1.sLeftKeyword2.value == "" )	{
                    alert("키워드를 입력해 주세요.");
                    document.leftShForm1.sLeftKeyword2.focus();
                    return;
                 }
                 //form.action = "/www/kor/util/search_result.do?skey=2&skeyword="+form.sLeftKeyword2.value;
                 form.setAttribute('action','/www/kor/util/search_result.do?skey=2&skeyword='+form.sLeftKeyword2.value);
                 form.submit();
            }
        </script>
    <div class="topWrap clearFix"><!-- Top -->
    <h2 class="skip">상단영역</h2>
    <div class="breadCrumb">
    <!-- LineMap -->
    <a href="/www/kor/main/main.do">홈</a> / <a href="/www/kor/findus/district.do">매장찾기</a> / <a class="current">지역별</a>
    <!-- //LineMap -->
    </div>
    <div class="rightCon">
    <div class="news">
    <h3>News</h3>
    <ul>
    <li><a href="/www/kor/board/view.do?board_seq=550"><span class="sbj">
                        
                            
                            
                                [이벤트 당첨자] 맥올데이 어택 당첨자 공지
                            
                        
                        </span><span class="date">2018.04.13</span></a></li>
    </ul>
    </div>
    <div class="lang">
    <a href="/www/eng/main/main.do">ENG</a>
    </div>
    </div>
    </div><!-- //Top -->
    <nav id="gnb"><!-- GNB -->
    <h2 class="skip">글로벌 네비게이션</h2>
    <ul class="d1">
    <li class="d1-1"><a href="/www/kor/menu/menu_list.do?cate_cd=100">메뉴</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2 odd">
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=100">버거</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=110">세트메뉴</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=140">맥모닝</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=130">행복의 나라 메뉴</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=180">해피밀<sub class="reg">®</sub></a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=150">스낵과 사이드</a></li>
    </ul>
    <ul class="d2 even">
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=190">맥카페</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=170">음료</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=160">디저트</a></li>
    <li><a href="http://www.mcdonalds.co.kr/uploadFolder/page/p_menu.jsp" onclick="NewWindow(this.href,'name','940','670','yes');return false" title="새창">맥딜리버리 메뉴</a></li>
    </ul>
    </div>
    </div>
    </li>
    <li class="d1-2"><a href="/www/kor/findus/district.do">매장찾기</a>
    <form action="/www/kor/findus/district.do" method="post" name="leftShForm"><!-- onkeypress="return event.keyCode!=13" -->
    <div class="submenu">
    <div class="inner">
    <fieldset>
    <legend>매장찾기</legend>
    <input id="sLeftKeyword1" name="sLeftKeyword1" onkeydown="EnterSubmit();" placeholder="동이름, 매장명을 검색해 주세요." title="매장찾기 - 동이름, 매장명으로 검색" type="text"/>
    <a class="btn_search" href="javascript:leftShSubmit();"><img alt="검색" src="/www/common/images/kor/common/header/btn_submit.gif"/></a>
    </fieldset>
    <ul class="d2">
    <li><a href="/www/kor/findus/district.do">지역별</a></li>
    <li><a href="/www/kor/findus/subway.do">지하철별</a></li>
    <li><a href="/www/kor/findus/delivery.do">맥딜리버리</a></li>
    <li><a href="/www/kor/findus/thru.do">맥드라이브</a></li>
    </ul>
    </div>
    </div>
    </form>
    </li>
    <li class="d1-3"><a href="/www/kor/event/event_view.do?event_seq=188">프로모션</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2">
    <li><a href="/www/kor/event/event_view.do?event_seq=188"><img alt="9/15(토) 맥드라이브 데이&lt;br&gt;★상하이 치킨 스낵랩★이 무료!" src="/uploadFolder/event/event_k_201808310547257290.jpg"/></a>
    <p class="evenTitle"><a href="/www/kor/event/event_view.do?event_seq=188">9/15(토) 맥드라이브 데이<br/>★상하이 치킨 스낵랩★이 무료!</a></p>
    </li>
    <li><a href="/www/kor/event/event_view.do?event_seq=181"><img alt="지금, 과일 한잔하자! 골든 키위 칠러 출시!" src="/uploadFolder/event/event_k_201808090540086250.jpg"/></a>
    <p class="evenTitle"><a href="/www/kor/event/event_view.do?event_seq=181">과일 칠러의 계절!<br/>골든 키위 칠러!</a></p>
    </li>
    </ul>
    </div>
    </div>
    </li>
    <li class="d1-16"><a href="/event/kor/pc/mc_allday.jsp">맥올데이 세트</a></li>
    <li class="d1-11"><a href="/event/kor/pc/happy_menu.jsp">행복의 나라 메뉴</a></li>
    <!-- 150811 -->
    <li class="d1-12"><a href="/event/kor/pc/signature_burger.jsp">시그니처 버거</a></li>
    <li class="d1-13"><a href="/event/kor/pc/people.jsp">맥도날드 사람들</a></li>
    <!-- 171012 -->
    <li class="d1-15"><a href="/event/kor/pc/farmrestaurant.jsp">맥도날드의 품질</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2">
    <li><a href="/event/kor/pc/farmrestaurant.jsp">농장에서 레스토랑까지</a></li>
    <li><a href="/event/kor/pc/NOD.jsp">맥도날드 주방 공개의 날</a></li>
    <li><a href="/event/kor/pc/faq.jsp">궁금한 모든 것을 알려드립니다.</a></li>
    </ul>
    </div>
    </div>
    </li>
    <li class="d1-4"><a href="/www/kor/story/history.do">맥도날드 이야기</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2">
    <li><a href="/www/kor/story/history.do">맥도날드의 역사</a></li>
    <li><a href="/www/kor/story/promise.do">맥도날드의 약속</a></li>
    <!-- <li><a href="/www/kor/story/q_campaign.do">맥도날드의 품질</a></li> -->
    <li><a href="/www/kor/story/eco.do">맥도날드의 환경이야기</a></li>
    <li><a href="/www/kor/story/society.do">맥도날드의 사회공헌</a></li>
    <li><a href="/event/kor/pc/safety.jsp">맥도날드 안전지킴 캠페인</a></li>
    <!-- <li><a href="/event/kor/pc/pyeongchang_2018.jsp">2018 평창 동계올림픽대회</a></li> -->
    <li><a href="/www/kor/board/list.do">새소식</a></li>
    </ul>
    </div>
    </div>
    </li>
    <li class="d1-5"><a href="/www/kor/findus/delivery.do">맥딜리버리</a></li>
    <li class="d1-6"><a href="/www/kor/findus/thru.do">맥드라이브</a></li>
    <li class="d1-7"><a href="/www/kor/recruit/recruit_person.do">인재채용</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2">
    <li><a href="/www/kor/recruit/recruit_person.do">맥도날드 문화</a></li>
    <li><a href="/www/kor/recruit/recruit_work.do">업무소개</a></li>
    <!-- <li><a href="/www/kor/recruit/recruit_istory.do">i-story</a></li> -->
    <li><a href="/www/kor/recruit/recruit_process.do">성장의 기회</a></li>
    <li><a href="/www/kor/recruit/apply_gate.do">채용공고 및 지원</a></li>
    <li><a href="http://www.mcdonalds-recruit.co.kr/recruit/recruit_confirmation.asp?pMenuCode=1001">결과확인</a></li>
    </ul>
    </div>
    </div>
    </li>
    <!-- <li class="d1-8"><a href="/www/kor/join/partner_success.do">가맹점 모집</a>
                    <div class="submenu">
                        <div class="inner">
                            <ul class="d2">
                                <li><a href="/www/kor/join/partner_success.do">성공요인</a></li>
                                <li><a href="/www/kor/join/partner_setup.do">개설절차 및 조건</a></li>
                                <li><a href="/www/kor/join/partner_case.do">성공 창업스토리</a></li>
                                <li><a href="/www/kor/join/apply_guide1.do">가맹설명회 신청</a></li>
                                <li><a href="/www/kor/join/partner_apply.do">지원서 작성</a></li>
                            </ul>
                        </div>
                    </div>
                </li> -->
    <li class="d1-9"><a href="/www/kor/store/store.do">임차의뢰</a></li>
    <li class="d1-14"><a href="https://voc.mcd.co.kr/MC/HOM/faqMain.jsp">고객문의</a></li>
    <li class="d1-10"><a href="/www/kor/util/search_result.do">검색</a>
    <form action="/www/kor/util/search_result.do" method="post" name="leftShForm1"><!-- onkeypress="return event.keyCode!=13" -->
    <div class="submenu">
    <div class="inner">
    <fieldset>
    <legend>통합검색</legend>
    <input id="sLeftKeyword2" name="sLeftKeyword2" onkeydown="EnterSubmit1();" placeholder="검색어를 입력해주세요" title="검색어를 입력해주세요" type="text"/>
    <a class="btn_search" href="javascript:leftShSubmit1();"><img alt="검색" src="/www/common/images/kor/common/header/btn_submit.gif"/></a>
    </fieldset>
    </div>
    </div>
    </form>
    </li>
    </ul>
    </nav><!-- //GNB -->
    </header><!-- //Header -->
    <div id="container"><!-- container -->
    <section class="findus" id="contents"><!-- contents -->
    <h2 class="skip">매장찾기</h2><!-- [ 2013-11-15 ] 수정 -->
    <div class="conBody district"><!-- conBody : 컨텐츠 내용 Start -->
    <ul class="find_tabmenu">
    <li class="current"><a href="/www/kor/findus/district.do">지역별</a></li>
    <li><a href="/www/kor/findus/subway.do">지하철별</a></li>
    <li class="red"><a href="/www/kor/findus/delivery.do">맥딜리버리</a></li>
    <li class="red"><a href="/www/kor/findus/thru.do">맥드라이브</a></li>
    </ul>
    <a class="btn_print" href="javascript:printBtn();" id="btnPrint"><img alt="인쇄" height="23" src="../../common/images/kor/common/btn/btn_print.gif" width="24"/></a><!-- [ 2013-11-15 ] 인쇄 버튼 위치 이동 -->
    <h3 class="skip">지역별 검색</h3><!-- [ 2013-11-15 ] 추가 -->
    <div class="searchArea">
    <form action="/www/kor/findus/district.do" method="get" name="shForm">
    <input id="sSearch_yn" name="sSearch_yn" type="hidden" value="Y"/>
    <table class="tbl-findus">
    <caption>매장찾기 지역별 검색 시 지역선택, 매장검색, 이용가능 서비스 정보</caption><!-- [ 2013-11-15 ] 수정 -->
    <colgroup>
    <col style="width:61px;"/>
    <col style="width:360px;"/>
    <col style="width:120px;"/>
    <col/>
    </colgroup>
    <tr>
    <th scope="row"><input id="skey_st" name="skey" type="hidden" value="2"/>매장검색</th>
    <td><input class="type-text" id="skeyword" name="skeyword" onkeydown="EnterSubmitLocal();" title="매장명, 동명, 도로명 입력" type="text" value="서울"/></td>
    <th rowspan="3" scope="row">이용가능 서비스</th>
    <td rowspan="3">
    <div class="inner"><!-- [ 2013-11-25 ] 수정 -->
    <input id="sflag1" name="sflag1" type="checkbox" value="-1-"/><label for="sflag1">24시간</label>
    <input id="sflag2" name="sflag2" type="checkbox" value="-2-"/><label for="sflag2">맥모닝</label>
    </div>
    <div class="inner">
    <input id="sflag3" name="sflag3" type="checkbox" value="-7-"/><label for="sflag3">맥올데이<i class="icon_allday"></i></label>
    <!-- <input type="checkbox" id="sflag3" name="sflag3"  value="-3-" /><label for="sflag3">맥카페</label> -->
    <input id="sflag4" name="sflag4" type="checkbox" value="-4-"/><label for="sflag4">맥딜리버리</label>
    </div>
    <div class="inner">
    <input id="sflag5" name="sflag5" type="checkbox" value="-5-"/><label for="sflag5">맥드라이브<i class="icon_drive"></i></label>
    <input id="sflag6" name="sflag6" type="checkbox" value="-6-"/><label for="sflag6">시그니처 버거<i class="icon_sign"></i></label>
    <!-- [2017-03-13] 수정 -->
    </div>
    </td>
    </tr>
    <tr>
    <th colspan="2" scope="row" style="font-size:0.96em;padding-left:60px;">
    							검색 안내 : 매장명, 동명, 도로명을 검색해 주세요.<br/>
    							검색 예시 : 을지로1가, 창천동 / 남대문로, 연세로 / 서울시청점, 연세대점
    							</th>
    </tr>
    </table>
    <!--  <p class="tip">검색어 또는 조건을 입력 후, 검색 버튼을 클릭!</p> -->
    <div class="btnWrap">
    <span class="btn"><span class="gray big"><a href="/www/kor/findus/district.do">초기화</a></span></span>
    <span class="btn"><span class="red big"><input onclick="shSubmit();" type="button" value="매장찾기"/></span></span>
    </div>
    </form>
    </div>
    <div id="print_div">
    <div class="mapArea"><!-- [ 2013-11-15 ] 수정 -->
    <!-- <p class="address">  (검색지역)</p> -->
    <div class="mapApi" id="map" style="width:887px;height:408px;"></div>
    </div>
    <div class="searchResult">
    <h3 class="skip">지역별 검색 결과</h3><!-- [ 2013-11-15 ] 수정 -->
    <ul class="listHeader clearFix">
    <li>매장명 / 전화번호 / 주소</li>
    <li>영업시간</li>
    <li>맥모닝</li>
    <!-- <li>맥카페</li> -->
    <li>맥올데이</li>
    <li>시그니처 버거</li>
    <li>맥딜리버리</li><!-- [2017-03-13] 수정 -->
    <li>맥드라이브</li><!-- [2017-05-08] 수정 -->
    </ul>
    <ul class="resultList"><!-- [2013-11-25 ]수정 -->
    <li>
    <div class="detail">
    <dl class="clearFix">
    <dt><a href="javascript:moveMap('37.494879','127.130762');"> <img alt="A" src="../../common/images/kor/findus/1.gif"/> 가락DT점</a></dt>
    <dd>070-7017-0622
                                                            , 070-7017-0613
                                                            
                                                        </dd>
    <dd>서울특별시 송파구 가락동 193-7</dd>
    <!-- 도로명 검색주소 노출 -->
    <dd class="road">[도로명주소]서울특별시 송파구 동남로 196 (가락동)</dd>
    <dd class="infoCheck">
    <table border="0" cellpadding="5" cellspacing="5">
    <colgroup>
    <col style="width:70px"/>
    <col style="width:65.8px"/>
    <!-- <col style="width:65.8px" /> -->
    <col style="width:75.1px"/>
    <col style="width:102px"/>
    <col style="width:87px"/>
    <col style="width:72px"/>
    </colgroup>
    <tbody>
    <tr>
    <td>
    																		
    																			
    																			
    																			
    																			07:00~01:00
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																		
    																	</td>
    <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td></td>
    <!-- <td></td> -->
    <td>
    																		
    																			
    																				
    																				
    																				
    																				
    																				07:00~01:00
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																			
    																		 
    																	</td>
    <td><img alt="맥드라이브 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    </tr>
    </tbody>
    </table>
    <!-- <span>
    															
    																
    																
    																
    																07:00~01:00
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    															
    														</span>
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                            <span></span>
                                                            <span>
    															
    																
    																	
    																	
    																	
    																	
    																	07:00~01:00
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																
    															 
    														</span>
    
    
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥드라이브 있음" /></span>
                                                            <span></span>
    														<span>
    														   
    															
    															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
    															
    															
    															
    															
    														</span> -->
    </dd>
    </dl>
    </div>
    </li>
    <li>
    <div class="detail">
    <dl class="clearFix">
    <dt><a href="javascript:moveMap('37.4813244','126.8837789');"> <img alt="B" src="../../common/images/kor/findus/2.gif"/> 가산디지털점</a></dt>
    <dd>070-7017-2448
                                                            , 070-7017-7448
                                                            
                                                        </dd>
    <dd>서울특별시 금천구 가산동 50-3 대륭포스트타워6차 1층</dd>
    <!-- 도로명 검색주소 노출 -->
    <dd class="road">[도로명주소]서울특별시 금천구 벚꽃로 298 (가산동)</dd>
    <dd class="infoCheck">
    <table border="0" cellpadding="5" cellspacing="5">
    <colgroup>
    <col style="width:70px"/>
    <col style="width:65.8px"/>
    <!-- <col style="width:65.8px" /> -->
    <col style="width:75.1px"/>
    <col style="width:102px"/>
    <col style="width:87px"/>
    <col style="width:72px"/>
    </colgroup>
    <tbody>
    <tr>
    <td>
    																		
    																			24시간
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																		
    																	</td>
    <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td><img alt="Signature Burger 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <!-- <td></td> -->
    <td>
    																		
    																			
    																				24시간
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																			
    																		 
    																	</td>
    <td></td>
    </tr>
    </tbody>
    </table>
    <!-- <span>
    															
    																24시간
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    															
    														</span>
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                            <span></span>
                                                            <span>
    															
    																
    																	24시간
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																
    															 
    														</span>
    
    
                                                            <span></span>
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="Signature Burger 있음" /></span>
    														<span>
    														   
    															
    															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
    															
    															
    															
    															
    														</span> -->
    </dd>
    </dl>
    </div>
    </li>
    <li>
    <div class="detail">
    <dl class="clearFix">
    <dt><a href="javascript:moveMap('37.4801705','126.8811402');"> <img alt="C" src="../../common/images/kor/findus/3.gif"/> 가산비지니스센터점</a></dt>
    <dd>070-7017-2433
                                                            , 070-7017-4433
                                                            
                                                        </dd>
    <dd>서울특별시 금천구 가산동 371-6 가산비지니스센터</dd>
    <!-- 도로명 검색주소 노출 -->
    <dd class="road">[도로명주소]서울특별시 금천구 가산디지털1로 165 (가산동)</dd>
    <dd class="infoCheck">
    <table border="0" cellpadding="5" cellspacing="5">
    <colgroup>
    <col style="width:70px"/>
    <col style="width:65.8px"/>
    <!-- <col style="width:65.8px" /> -->
    <col style="width:75.1px"/>
    <col style="width:102px"/>
    <col style="width:87px"/>
    <col style="width:72px"/>
    </colgroup>
    <tbody>
    <tr>
    <td>
    																		
    																			
    																			
    																			07:00~00:00
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																		
    																	</td>
    <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td><img alt="Signature Burger 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <!-- <td></td> -->
    <td>
    																		
    																			
    																				
    																				
    																				
    																				07:00~00:00
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																			
    																		 
    																	</td>
    <td></td>
    </tr>
    </tbody>
    </table>
    <!-- <span>
    															
    																
    																
    																07:00~00:00
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    															
    														</span>
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                            <span></span>
                                                            <span>
    															
    																
    																	
    																	
    																	
    																	07:00~00:00
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																
    															 
    														</span>
    
    
                                                            <span></span>
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="Signature Burger 있음" /></span>
    														<span>
    														   
    															
    															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
    															
    															
    															
    															
    														</span> -->
    </dd>
    </dl>
    </div>
    </li>
    <li>
    <div class="detail">
    <dl class="clearFix">
    <dt><a href="javascript:moveMap('37.4986859','127.0287553');"> <img alt="D" src="../../common/images/kor/findus/4.gif"/> 강남2호점</a></dt>
    <dd>070-7017-6865
                                                            , 070-7204-3278
                                                            
                                                        </dd>
    <dd>서울특별시 강남구 역삼동 822-2 비전타워 2층</dd>
    <!-- 도로명 검색주소 노출 -->
    <dd class="road">[도로명주소]서울특별시 강남구 테헤란로 107, 2층 (역삼동)</dd>
    <dd class="infoCheck">
    <table border="0" cellpadding="5" cellspacing="5">
    <colgroup>
    <col style="width:70px"/>
    <col style="width:65.8px"/>
    <!-- <col style="width:65.8px" /> -->
    <col style="width:75.1px"/>
    <col style="width:102px"/>
    <col style="width:87px"/>
    <col style="width:72px"/>
    </colgroup>
    <tbody>
    <tr>
    <td>
    																		
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			08:00~24:00
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																		
    																	</td>
    <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td><img alt="Signature Burger 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <!-- <td></td> -->
    <td>
    																		
    																			
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				08:00~24:00
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																			
    																		 
    																	</td>
    <td></td>
    </tr>
    </tbody>
    </table>
    <!-- <span>
    															
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																08:00~24:00
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    															
    														</span>
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                            <span></span>
                                                            <span>
    															
    																
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																
    															 
    														</span>
    
    
                                                            <span></span>
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="Signature Burger 있음" /></span>
    														<span>
    														   
    															
    															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
    															
    															
    															
    															
    														</span> -->
    </dd>
    </dl>
    </div>
    </li>
    <li>
    <div class="detail">
    <dl class="clearFix">
    <dt><a href="javascript:moveMap('37.5162358','127.0413134');"> <img alt="E" src="../../common/images/kor/findus/5.gif"/> 강남구청점</a></dt>
    <dd>070-7017-4454
                                                            , 070-7017-4547
                                                            
                                                        </dd>
    <dd>서울특별시 강남구 논현동 242-29</dd>
    <!-- 도로명 검색주소 노출 -->
    <dd class="road">[도로명주소]서울특별시 강남구 선릉로 667 (논현동)</dd>
    <dd class="infoCheck">
    <table border="0" cellpadding="5" cellspacing="5">
    <colgroup>
    <col style="width:70px"/>
    <col style="width:65.8px"/>
    <!-- <col style="width:65.8px" /> -->
    <col style="width:75.1px"/>
    <col style="width:102px"/>
    <col style="width:87px"/>
    <col style="width:72px"/>
    </colgroup>
    <tbody>
    <tr>
    <td>
    																		
    																			24시간
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																			
    																		
    																	</td>
    <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <td><img alt="Signature Burger 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
    <!-- <td></td> -->
    <td>
    																		
    																			
    																				24시간
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																				
    																			
    																		 
    																	</td>
    <td></td>
    </tr>
    </tbody>
    </table>
    <!-- <span>
    															
    																24시간
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    																
    															
    														</span>
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                            <span></span>
                                                            <span>
    															
    																
    																	24시간
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																	
    																
    															 
    														</span>
    
    
                                                            <span></span>
                                                            <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="Signature Burger 있음" /></span>
    														<span>
    														   
    															
    															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
    															
    															
    															
    															
    														</span> -->
    </dd>
    </dl>
    </div>
    </li>
    </ul>
    <div class="paging">
    <a class="btn_first"><img alt="처음" src="../../common/images/kor/common/board/btn_first_off.gif"/></a>
    <a class="btn_prev"><img alt="이전" src="../../common/images/kor/common/board/btn_prev_off.gif"/></a>
    <a class="current">1</a>
    <a href="?pageIndex=2&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N">2</a>
    <a href="?pageIndex=3&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N">3</a>
    <a href="?pageIndex=4&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N">4</a>
    <a href="?pageIndex=5&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N">5</a>
    <a class="btn_next" href="?pageIndex=6&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N"><img alt="다음" src="../../common/images/kor/common/board/btn_next_on.gif"/></a>
    <a class="btn_last" href="?pageIndex=21&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N"><img alt="마지막" src="../../common/images/kor/common/board/btn_last_on.gif"/></a>
    </div>
    </div>
    </div>
    </div><!-- conBody : 컨텐츠 내용 End -->
    </section><!-- //contents-->
    <footer class="footWhite" id="footer"><!-- footer -->
    <div class="inner">
    <h2 class="skip">하단영역</h2>
    <div class="sns">
    <div id="fb-root"></div>
    <script>
                            (function(d, s, id) {
                                var js, fjs = d.getElementsByTagName(s)[0];
                                if (d.getElementById(id)) return;
                                js = d.createElement(s); js.id = id;
                                js.src = "//connect.facebook.net/ko_KR/all.js#xfbml=1";
                                fjs.parentNode.insertBefore(js, fjs);
                            }(document, 'script', 'facebook-jssdk'));
                        </script>
    <!-- SNS ICON -->
    <a href="http://www.facebook.com/McDonaldsKorea" id="sns01" onclick="_gaq.push(['_trackEvent', 'PC_SNS_FB', 'click']);" target="_blank"><img alt="페이스북" src="/www/common/images/kor/common/footer/ico_sns01.png"/></a>
    <a href="http://instagram.com/mcdonalds_kr" id="sns02" onclick="_gaq.push(['_trackEvent', 'PC_SNS_INS', 'click']);" target="_blank"><img alt="인스타" src="/www/common/images/kor/common/footer/ico_sns02.png"/></a>
    <a href="http://www.youtube.com/McDonaldsKor" id="sns03" onclick="_gaq.push(['_trackEvent', 'PC_SNS_YTB', 'click']);" target="_blank"><img alt="유튜브" src="/www/common/images/kor/common/footer/ico_sns03.png"/></a>
    <a href="http://story.kakao.com/ch/mcdonalds/feed" id="sns04" onclick="_gaq.push(['_trackEvent', 'PC_SNS_KS', 'click']);" target="_blank"><img alt="카카오스토리" src="/www/common/images/kor/common/footer/ico_sns04.png"/></a>
    <!-- //SNS ICON -->
    <!-- 페북
                        <div class="fb-like" data-href="https://www.facebook.com/McDonaldsKorea" data-layout="button_count" data-action="like" data-show-faces="false" data-share="false"></div>
                        <!-- 인스타
                        <a id="insta" href="http://instagram.com/mcdonalds_kr?ref=badge">
                        	<img src="/www/common/images/kor/common/footer/ico_Insta.png" alt="Instagram" /></a>
                        <!-- 카스 
                        <div id="kakaostory-follow-button" data-id="mcdonalds" data-type="horizontal" data-show-follower-count="true"></div>
                        
                        <!-- 유튜브
                        <a href="http://www.youtube.com/user/McDonaldsKor" class="btn_yTube" target="_blank" title="새창"><img src="/www/common/images/kor/common/btn/btn_youtube.png" width="42" height="20" alt="YouTube" /></a>
                        -->
    <!-- 접근성 -->
    <a class="btn_waMark" href="http://webwatch.or.kr/certification/int_purpose.html" target="_blank" title="새창"><img alt="WA 웹접근성 인증마크" src="/www/common/images/kor/common/footer/waMark.png"/></a>
    </div>
    <div class="footRight">
    <ul class="footMenu">
    <li><a href="https://voc.mcd.co.kr/MC/HOM/faqMain.jsp" onclick="window.open(this.href,'','width=1003px, height=800px'); return false;" target="_blank" title="새창">1:1 문의 및 칭찬</a></li>
    <li><a href="/www/kor/util/private.do"><span class="private_bold">개인정보 취급방침</span></a></li>
    <li><a href="/www/kor/util/sitemap.do">사이트맵</a></li>
    </ul>
    <div class="footInfo">
    <p class="info">한국맥도날드(유) l 대표자: 조주연 l 사업자등록번호: 101-81-26409</p>
    <p class="copy">전화주문 : 1600-5252 ㅣCOPYRIGHT ⓒ 2014 ALL RIGHTS RESERVED BY McDonald's</p>
    <p class="right_txt" style="margin-top:10px; line-height:18px;">당사 홈페이지의 이미지나 내용을 외부로 가져가서 사용하는 행위는 당사의 저작권, 상표권 등 지식재산권을 침해하는 행위입니다.<br/>
                            	무단 공유할 경우 저작권법, 부정경쟁방지법 기타 관련 법령에 따라 책임지게 될 수 있음을 알려 드립니다.<br/>
                            	관련한 질의사항은 고객센터로 문의해 주시기 바랍니다.
                      </p>
    </div>
    </div>
    </div>
    <!-- Google Analytics -->
    <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    
    ga('create', 'UA-15032749-2', 'auto');  // Replace with your property ID.
    ga('create', 'UA-15032749-4', 'auto', 'clientTracker');
    
    ga('send', 'pageview');
    ga('clientTracker.send', 'pageview');
    
    </script>
    <!-- End Google Analytics -->
    <script type="text/javascript">
    
    /* 20170410_구글 코드 구 버전
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-15032749-2']);
      _gaq.push(['_trackPageview']);
    
      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();
    
    */
    
    /* staging
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-15032749-8']);
    _gaq.push(['_trackPageview']);
    
    (function() {
      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    */
    
    /* 카카오스토리 */
    window.kakaoAsyncInit = function () {
        Kakao.Story.createFollowButton({
          container: '#kakaostory-follow-button'
        });
      };
    
      (function (d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//developers.kakao.com/sdk/js/kakao.story.min.js";
        fjs.parentNode.insertBefore(js, fjs);
      }(document, 'script', 'kakao-js-sdk'));
    /* 카카오스토리 */
    </script>
    </footer><!-- //footer -->
    </div><!-- //container -->
    </div><!-- wrap -->
    </body>
    </html>




```python
tmp = soup.find_all('dl','clearFix')
tmp
```




    [<dl class="clearFix">
     <dt><a href="javascript:moveMap('37.494879','127.130762');"> <img alt="A" src="../../common/images/kor/findus/1.gif"/> 가락DT점</a></dt>
     <dd>070-7017-0622
                                                             , 070-7017-0613
                                                             
                                                         </dd>
     <dd>서울특별시 송파구 가락동 193-7</dd>
     <!-- 도로명 검색주소 노출 -->
     <dd class="road">[도로명주소]서울특별시 송파구 동남로 196 (가락동)</dd>
     <dd class="infoCheck">
     <table border="0" cellpadding="5" cellspacing="5">
     <colgroup>
     <col style="width:70px"/>
     <col style="width:65.8px"/>
     <!-- <col style="width:65.8px" /> -->
     <col style="width:75.1px"/>
     <col style="width:102px"/>
     <col style="width:87px"/>
     <col style="width:72px"/>
     </colgroup>
     <tbody>
     <tr>
     <td>
     																		
     																			
     																			
     																			
     																			07:00~01:00
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																		
     																	</td>
     <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td></td>
     <!-- <td></td> -->
     <td>
     																		
     																			
     																				
     																				
     																				
     																				
     																				07:00~01:00
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																			
     																		 
     																	</td>
     <td><img alt="맥드라이브 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     </tr>
     </tbody>
     </table>
     <!-- <span>
     															
     																
     																
     																
     																07:00~01:00
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     															
     														</span>
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                             <span></span>
                                                             <span>
     															
     																
     																	
     																	
     																	
     																	
     																	07:00~01:00
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																
     															 
     														</span>
     
     
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥드라이브 있음" /></span>
                                                             <span></span>
     														<span>
     														   
     															
     															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
     															
     															
     															
     															
     														</span> -->
     </dd>
     </dl>, <dl class="clearFix">
     <dt><a href="javascript:moveMap('37.4813244','126.8837789');"> <img alt="B" src="../../common/images/kor/findus/2.gif"/> 가산디지털점</a></dt>
     <dd>070-7017-2448
                                                             , 070-7017-7448
                                                             
                                                         </dd>
     <dd>서울특별시 금천구 가산동 50-3 대륭포스트타워6차 1층</dd>
     <!-- 도로명 검색주소 노출 -->
     <dd class="road">[도로명주소]서울특별시 금천구 벚꽃로 298 (가산동)</dd>
     <dd class="infoCheck">
     <table border="0" cellpadding="5" cellspacing="5">
     <colgroup>
     <col style="width:70px"/>
     <col style="width:65.8px"/>
     <!-- <col style="width:65.8px" /> -->
     <col style="width:75.1px"/>
     <col style="width:102px"/>
     <col style="width:87px"/>
     <col style="width:72px"/>
     </colgroup>
     <tbody>
     <tr>
     <td>
     																		
     																			24시간
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																		
     																	</td>
     <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td><img alt="Signature Burger 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <!-- <td></td> -->
     <td>
     																		
     																			
     																				24시간
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																			
     																		 
     																	</td>
     <td></td>
     </tr>
     </tbody>
     </table>
     <!-- <span>
     															
     																24시간
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     															
     														</span>
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                             <span></span>
                                                             <span>
     															
     																
     																	24시간
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																
     															 
     														</span>
     
     
                                                             <span></span>
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="Signature Burger 있음" /></span>
     														<span>
     														   
     															
     															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
     															
     															
     															
     															
     														</span> -->
     </dd>
     </dl>, <dl class="clearFix">
     <dt><a href="javascript:moveMap('37.4801705','126.8811402');"> <img alt="C" src="../../common/images/kor/findus/3.gif"/> 가산비지니스센터점</a></dt>
     <dd>070-7017-2433
                                                             , 070-7017-4433
                                                             
                                                         </dd>
     <dd>서울특별시 금천구 가산동 371-6 가산비지니스센터</dd>
     <!-- 도로명 검색주소 노출 -->
     <dd class="road">[도로명주소]서울특별시 금천구 가산디지털1로 165 (가산동)</dd>
     <dd class="infoCheck">
     <table border="0" cellpadding="5" cellspacing="5">
     <colgroup>
     <col style="width:70px"/>
     <col style="width:65.8px"/>
     <!-- <col style="width:65.8px" /> -->
     <col style="width:75.1px"/>
     <col style="width:102px"/>
     <col style="width:87px"/>
     <col style="width:72px"/>
     </colgroup>
     <tbody>
     <tr>
     <td>
     																		
     																			
     																			
     																			07:00~00:00
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																		
     																	</td>
     <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td><img alt="Signature Burger 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <!-- <td></td> -->
     <td>
     																		
     																			
     																				
     																				
     																				
     																				07:00~00:00
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																			
     																		 
     																	</td>
     <td></td>
     </tr>
     </tbody>
     </table>
     <!-- <span>
     															
     																
     																
     																07:00~00:00
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     															
     														</span>
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                             <span></span>
                                                             <span>
     															
     																
     																	
     																	
     																	
     																	07:00~00:00
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																
     															 
     														</span>
     
     
                                                             <span></span>
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="Signature Burger 있음" /></span>
     														<span>
     														   
     															
     															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
     															
     															
     															
     															
     														</span> -->
     </dd>
     </dl>, <dl class="clearFix">
     <dt><a href="javascript:moveMap('37.4986859','127.0287553');"> <img alt="D" src="../../common/images/kor/findus/4.gif"/> 강남2호점</a></dt>
     <dd>070-7017-6865
                                                             , 070-7204-3278
                                                             
                                                         </dd>
     <dd>서울특별시 강남구 역삼동 822-2 비전타워 2층</dd>
     <!-- 도로명 검색주소 노출 -->
     <dd class="road">[도로명주소]서울특별시 강남구 테헤란로 107, 2층 (역삼동)</dd>
     <dd class="infoCheck">
     <table border="0" cellpadding="5" cellspacing="5">
     <colgroup>
     <col style="width:70px"/>
     <col style="width:65.8px"/>
     <!-- <col style="width:65.8px" /> -->
     <col style="width:75.1px"/>
     <col style="width:102px"/>
     <col style="width:87px"/>
     <col style="width:72px"/>
     </colgroup>
     <tbody>
     <tr>
     <td>
     																		
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			08:00~24:00
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																		
     																	</td>
     <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td><img alt="Signature Burger 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <!-- <td></td> -->
     <td>
     																		
     																			
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				08:00~24:00
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																			
     																		 
     																	</td>
     <td></td>
     </tr>
     </tbody>
     </table>
     <!-- <span>
     															
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																08:00~24:00
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     															
     														</span>
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                             <span></span>
                                                             <span>
     															
     																
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																
     															 
     														</span>
     
     
                                                             <span></span>
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="Signature Burger 있음" /></span>
     														<span>
     														   
     															
     															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
     															
     															
     															
     															
     														</span> -->
     </dd>
     </dl>, <dl class="clearFix">
     <dt><a href="javascript:moveMap('37.5162358','127.0413134');"> <img alt="E" src="../../common/images/kor/findus/5.gif"/> 강남구청점</a></dt>
     <dd>070-7017-4454
                                                             , 070-7017-4547
                                                             
                                                         </dd>
     <dd>서울특별시 강남구 논현동 242-29</dd>
     <!-- 도로명 검색주소 노출 -->
     <dd class="road">[도로명주소]서울특별시 강남구 선릉로 667 (논현동)</dd>
     <dd class="infoCheck">
     <table border="0" cellpadding="5" cellspacing="5">
     <colgroup>
     <col style="width:70px"/>
     <col style="width:65.8px"/>
     <!-- <col style="width:65.8px" /> -->
     <col style="width:75.1px"/>
     <col style="width:102px"/>
     <col style="width:87px"/>
     <col style="width:72px"/>
     </colgroup>
     <tbody>
     <tr>
     <td>
     																		
     																			24시간
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																			
     																		
     																	</td>
     <td><img alt="맥모닝 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td><img alt="맥올데이 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <td><img alt="Signature Burger 있음" src="../../common/images/kor/common/ico/ico_check.gif"/></td>
     <!-- <td></td> -->
     <td>
     																		
     																			
     																				24시간
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																				
     																			
     																		 
     																	</td>
     <td></td>
     </tr>
     </tbody>
     </table>
     <!-- <span>
     															
     																24시간
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     																
     															
     														</span>
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥모닝 있음" /></span>
                                                             <span></span>
                                                             <span>
     															
     																
     																	24시간
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																	
     																
     															 
     														</span>
     
     
                                                             <span></span>
                                                             <span><img src="../../common/images/kor/common/ico/ico_check.gif" alt="Signature Burger 있음" /></span>
     														<span>
     														   
     															
     															   <img src="../../common/images/kor/common/ico/ico_check.gif" alt="맥런치 있음" />
     															
     															
     															
     															
     														</span> -->
     </dd>
     </dl>]




```python
len(tmp)
```




    5




```python
tmp2 = tmp[0].get_text()
tmp2
```




    '\n  가락DT점\n070-7017-0622\r\n                                                        , 070-7017-0613\r\n                                                        \r\n                                                    \n서울특별시 송파구 가락동 193-7\n\n[도로명주소]서울특별시 송파구 동남로 196 (가락동)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t07:00~01:00\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n\n\n\n\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t07:00~01:00\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n\n\n\n\n\n'




```python
tmp3 = tmp2.split('\n')
tmp3
```




    ['',
     '  가락DT점',
     '070-7017-0622\r',
     '                                                        , 070-7017-0613\r',
     '                                                        \r',
     '                                                    ',
     '서울특별시 송파구 가락동 193-7',
     '',
     '[도로명주소]서울특별시 송파구 동남로 196 (가락동)',
     '',
     '',
     '',
     '',
     '',
     '',
     '',
     '',
     '',
     '',
     '',
     '',
     '',
     '\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t07:00~01:00\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',
     '',
     '',
     '',
     '',
     '\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t07:00~01:00\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \r',
     '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',
     '',
     '',
     '',
     '',
     '',
     '',
     '']




```python
tmp3[1], tmp3[6], tmp3[8]
```




    ('  가락DT점', '서울특별시 송파구 가락동 193-7', '[도로명주소]서울특별시 송파구 동남로 196 (가락동)')




```python
tmp3[1].replace(' ', '')
```




    '가락DT점'




```python
response = urlopen(html.format(page=25))

soup = BeautifulSoup(response, "lxml")
soup
```




    <!DOCTYPE html>
    <html lang="ko">
    <head>
    <meta charset="utf-8"/>
    <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
    <meta content="소시지맥머핀, 듀엣세트, 맥도날드듀엣세트, 소세지맥머핀, 맥머핀, 에그맥머핀, 베이컨에그맥머핀, 소시지에그맥머핀, 아침배달음식, 브런치배달, 아침밥배달, 아침식사, 주말아침, 주말아침식사, 맥모닝, 맥딜리버리, 간단한아침식사, 간단한아침식사배달, 아침도시락배달, 아침배달, 아침식사배달, 아침식사배달업체, 주말간단한아침메뉴, 주말아침배달, 주말아침식사배달, 브런치메뉴, 브런치추천, 아침, 아침식사메뉴, 아침메뉴, 간단한아침메뉴, 아침대용식, 빅브렉퍼스트" name="description"/>
    <title>지역별 - McDonald's</title>
    <link href="/www/common/images/favicon.ico" rel="shortcut icon"/>
    <link href="../../common/css/normalize.css" rel="stylesheet" type="text/css"/>
    <link href="../../common/css/common.css" rel="stylesheet" type="text/css"/>
    <link href="../../common/css/sub.css" rel="stylesheet" type="text/css"/>
    <script src="../../common/js_ui/lib/jquery-1.10.2.min.js" type="text/javascript"></script>
    <script src="../../common/js_ui/lib/jquery.textPlaceholder.js" type="text/javascript"></script>
    <script src="../../common/js_ui/lib/html5shiv-printshiv.js" type="text/javascript"></script>
    <script src="../../common/js_ui/mcd_ui.js" type="text/javascript"></script>
    <script type="text/javascript">
    	var mobileKeyWords = new Array('iPhone', 'iPod', 'BlackBerry', 'Android', 'Windows CE', 'LG', 'MOT', 'SAMSUNG', 'SonyEricsson');
    	for (var word in mobileKeyWords){
    		if (navigator.userAgent.match(mobileKeyWords[word]) != null){
    			location.href = "http://m.mcdonalds.co.kr/me/kor/findus/district.do";
    		break;
    		}
     	}
    </script>
    <!--[if lt IE 9]>
        <script type="text/javascript">
            document.createElement("header"); document.createElement("nav"); document.createElement("section"); document.createElement("article"); document.createElement("footer");
        </script>
    <![endif]-->
    <script>
    function shGugunAjax(sobj,tobj,tagid){
    
        $.ajax({
            url : "/www/kor/ajax/ajax.usr_gugun.do",
            type : "POST",
            data : {"sido" : $("#"+sobj).val() , "tagid" : tagid} ,
            dataType : "text",
            success : function(response) {
                if(response != "") {
                    $("#"+tobj).html(response);
                    return;
                }
            },
            error : function(request, status, error) {
                if (request.status != '0') {
                    alert("code : " + request.status + "\r\nmessage : "
                        + request.reponseText + "\r\nerror : " + error);
                }
            }
        });
    }
    </script>
    <script charset="utf-8" src="http://apis.daum.net/maps/maps3.js?apikey=dd4031904c7964687d86513ffbcad30cb714e287" type="text/javascript"></script>
    <script type="text/javascript">
        var map;
        window.onload = function () {
    
            var latitude = "";
            var longitude = "";
    
            
                
                    
                
                
            
    
            map = new daum.maps.Map(document.getElementById('map'), {
                center: new daum.maps.LatLng(latitude,longitude),
                level: 7
            });
    
            var points = [
                
                    
                        
                    
                
            ];
            var icon = [
                
                    
                        
                    
                
            ];
    
            //######## Zooming, 지도/스카이 뷰 start ########
            var zoomControl = new daum.maps.ZoomControl();
            map.addControl(zoomControl, daum.maps.ControlPosition.RIGHT);
            var mapTypeControl = new daum.maps.MapTypeControl();
            map.addControl(mapTypeControl, daum.maps.ControlPosition.TOPRIGHT);
            //######## Zooming, 지도/스카이 뷰 End ########
    
    
            for(var i = 0; i < points.length; i++){
                new daum.maps.Marker({
                    position: points[i],
                    image: icon[i]
                }).setMap(map);
            }
        }
    
        function EnterSubmitLocal() {
            if(event.keyCode == 13) {
                shSubmit();
            }
        }
    
        function shSubmit(){
            document.shForm.submit();
        }
    
        function printBtn(){
            print();
        }
    
        function shSubmit(){
            var form = document.shForm;
            if ($("#skeyword").val() == "") {
    			alert("매장명, 동명, 도로명을 입력하세요");
    			$("#skeyword").focus();
    			return;
    		} else {
    			form.submit();
    	        return;
    		}
        }
    
        function moveMap(xx,yy){
            var po = new daum.maps.LatLng(xx, yy);
            map.setCenter(po);
        }
    
        function radioCheck(_gubun) {
            if (_gubun == "1") {
    			$("#skey4 option:eq(0)").attr("selected", "selected");
    			var opt2 = $("#skey5 option").size();
    			for(var i=1;i<opt2;i++)
    			{
    				$("#skey5 option:last").remove();
    			}
                $("#skeyword1").val("");
                $("#skeyword").val("");
                $("#skeyword2").val("");
            } else if(_gubun == "2"){
    			$("#skey1 option:eq(0)").attr("selected", "selected");
    			$("#skey4 option:eq(0)").attr("selected", "selected");
    			var opt1 = $("#skey2 option").size();
    			for(var i=1;i<opt1;i++)
    			{
    				$("#skey2 option:last").remove();
    			}
    			var opt2 = $("#skey5 option").size();
    			for(var i=1;i<opt2;i++)
    			{
    				$("#skey5 option:last").remove();
    			}
                $("#skeyword1").val("");
                $("#skeyword2").val("");
            } else if(_gubun == "3"){
    			$("#skey1 option:eq(0)").attr("selected", "selected");
    			var opt1 = $("#skey2 option").size();
    			for(var i=1;i<opt1;i++)
    			{
    				$("#skey2 option:last").remove();
    			}
                $("#skeyword").val("");
                $("#skeyword1").val("");
            }
            $('input:radio[name="skey"]:input[value="' + _gubun + '"]').prop("checked", true);
        }
    </script>
    <style>
    .searchResult ul.listHeader li{width:auto;padding:0 15px 13px}
    .searchResult ul.listHeader li:first-child{width:200px;}
    .searchResult ul.listHeader li:last-child{padding-right:0}
    .searchResult ul.resultList li div.detail{padding:0 0 0 10px}
    .searchResult ul.resultList li dl dd{width:178px;padding-left:20px;line-height:19px;letter-spacing:-0.3px;text-align:justify}
    .searchResult ul.resultList li dl dd.infoCheck span{vertical-align:top}
    .searchResult ul.resultList li dl dd.infoCheck{width:572px}
    span.except {display: block !important;clear: both;width:59px !important;color: #ae0b0c;margin:0 auto}
    </style>
    </head>
    <body class="findusBg">
    <!-- WIDERPLANET  SCRIPT START 2015.4.17 -->
    <div id="wp_tg_cts" style="display:none;"></div>
    <script type="text/javascript">
    var wptg_tagscript_vars = wptg_tagscript_vars || [];
    wptg_tagscript_vars.push(
    (function() {
    return {
               ti:"21843",         /*광고주 코드*/
               ty:"Home",         /*트래킹태그 타입*/
               device:"web"      /*디바이스 종류 (web 또는 mobile)*/
    };
    }));
    </script>
    <script async="" src="//astg.widerplanet.com/js/wp_astg_3.0.js" type="text/javascript"></script>
    <!-- // WIDERPLANET  SCRIPT END 2015.4.17 -->
    <div class="skipNavigation">
    <a href="#contents">본문바로가기</a>
    <a href="#gnb">글로벌 네비게이션</a>
    <a href="#footer">하단영역</a>
    </div>
    <div id="wrap"><!-- wrap -->
    <header id="header"><!-- Header -->
    <h1><a href="/www/kor/main/main.do"><img alt="I’m lovin’ it" height="95" src="/www/common/images/kor/common/header/logo.png" width="105"/></a></h1>
    <script>
            function EnterSubmit() {
                if(event.keyCode == 13) {
                    leftShSubmit();
                }
            }
            function EnterSubmit1() {
                if(event.keyCode == 13) {
                    leftShSubmit1();
                }
            }
            function leftShSubmit(){
                var form = document.leftShForm;
                if (form.sLeftKeyword1.value == "" )	{
                    alert("키워드를 입력해 주세요.");
                    form.sLeftKeyword1.focus();
                    return;
                }
                //form.action = "/www/kor/findus/district.do?sSearch_yn=Y&skey=2&skeyword="+document.leftShForm.sLeftKeyword1.value;
                form.setAttribute('action','/www/kor/findus/district.do?sSearch_yn=Y&skey=2&skeyword='+form.sLeftKeyword1.value);
                form.submit();
            }
            function leftShSubmit1(){
                var form = document.leftShForm1;
                if (document.leftShForm1.sLeftKeyword2.value == "" )	{
                    alert("키워드를 입력해 주세요.");
                    document.leftShForm1.sLeftKeyword2.focus();
                    return;
                 }
                 //form.action = "/www/kor/util/search_result.do?skey=2&skeyword="+form.sLeftKeyword2.value;
                 form.setAttribute('action','/www/kor/util/search_result.do?skey=2&skeyword='+form.sLeftKeyword2.value);
                 form.submit();
            }
        </script>
    <div class="topWrap clearFix"><!-- Top -->
    <h2 class="skip">상단영역</h2>
    <div class="breadCrumb">
    <!-- LineMap -->
    <a href="/www/kor/main/main.do">홈</a> / <a href="/www/kor/findus/district.do">매장찾기</a> / <a class="current">지역별</a>
    <!-- //LineMap -->
    </div>
    <div class="rightCon">
    <div class="news">
    <h3>News</h3>
    <ul>
    <li><a href="/www/kor/board/view.do?board_seq=550"><span class="sbj">
                        
                            
                            
                                [이벤트 당첨자] 맥올데이 어택 당첨자 공지
                            
                        
                        </span><span class="date">2018.04.13</span></a></li>
    </ul>
    </div>
    <div class="lang">
    <a href="/www/eng/main/main.do">ENG</a>
    </div>
    </div>
    </div><!-- //Top -->
    <nav id="gnb"><!-- GNB -->
    <h2 class="skip">글로벌 네비게이션</h2>
    <ul class="d1">
    <li class="d1-1"><a href="/www/kor/menu/menu_list.do?cate_cd=100">메뉴</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2 odd">
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=100">버거</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=110">세트메뉴</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=140">맥모닝</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=130">행복의 나라 메뉴</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=180">해피밀<sub class="reg">®</sub></a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=150">스낵과 사이드</a></li>
    </ul>
    <ul class="d2 even">
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=190">맥카페</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=170">음료</a></li>
    <li><a href="/www/kor/menu/menu_list.do?cate_cd=160">디저트</a></li>
    <li><a href="http://www.mcdonalds.co.kr/uploadFolder/page/p_menu.jsp" onclick="NewWindow(this.href,'name','940','670','yes');return false" title="새창">맥딜리버리 메뉴</a></li>
    </ul>
    </div>
    </div>
    </li>
    <li class="d1-2"><a href="/www/kor/findus/district.do">매장찾기</a>
    <form action="/www/kor/findus/district.do" method="post" name="leftShForm"><!-- onkeypress="return event.keyCode!=13" -->
    <div class="submenu">
    <div class="inner">
    <fieldset>
    <legend>매장찾기</legend>
    <input id="sLeftKeyword1" name="sLeftKeyword1" onkeydown="EnterSubmit();" placeholder="동이름, 매장명을 검색해 주세요." title="매장찾기 - 동이름, 매장명으로 검색" type="text"/>
    <a class="btn_search" href="javascript:leftShSubmit();"><img alt="검색" src="/www/common/images/kor/common/header/btn_submit.gif"/></a>
    </fieldset>
    <ul class="d2">
    <li><a href="/www/kor/findus/district.do">지역별</a></li>
    <li><a href="/www/kor/findus/subway.do">지하철별</a></li>
    <li><a href="/www/kor/findus/delivery.do">맥딜리버리</a></li>
    <li><a href="/www/kor/findus/thru.do">맥드라이브</a></li>
    </ul>
    </div>
    </div>
    </form>
    </li>
    <li class="d1-3"><a href="/www/kor/event/event_view.do?event_seq=188">프로모션</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2">
    <li><a href="/www/kor/event/event_view.do?event_seq=188"><img alt="9/15(토) 맥드라이브 데이&lt;br&gt;★상하이 치킨 스낵랩★이 무료!" src="/uploadFolder/event/event_k_201808310547257290.jpg"/></a>
    <p class="evenTitle"><a href="/www/kor/event/event_view.do?event_seq=188">9/15(토) 맥드라이브 데이<br/>★상하이 치킨 스낵랩★이 무료!</a></p>
    </li>
    <li><a href="/www/kor/event/event_view.do?event_seq=181"><img alt="지금, 과일 한잔하자! 골든 키위 칠러 출시!" src="/uploadFolder/event/event_k_201808090540086250.jpg"/></a>
    <p class="evenTitle"><a href="/www/kor/event/event_view.do?event_seq=181">과일 칠러의 계절!<br/>골든 키위 칠러!</a></p>
    </li>
    </ul>
    </div>
    </div>
    </li>
    <li class="d1-16"><a href="/event/kor/pc/mc_allday.jsp">맥올데이 세트</a></li>
    <li class="d1-11"><a href="/event/kor/pc/happy_menu.jsp">행복의 나라 메뉴</a></li>
    <!-- 150811 -->
    <li class="d1-12"><a href="/event/kor/pc/signature_burger.jsp">시그니처 버거</a></li>
    <li class="d1-13"><a href="/event/kor/pc/people.jsp">맥도날드 사람들</a></li>
    <!-- 171012 -->
    <li class="d1-15"><a href="/event/kor/pc/farmrestaurant.jsp">맥도날드의 품질</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2">
    <li><a href="/event/kor/pc/farmrestaurant.jsp">농장에서 레스토랑까지</a></li>
    <li><a href="/event/kor/pc/NOD.jsp">맥도날드 주방 공개의 날</a></li>
    <li><a href="/event/kor/pc/faq.jsp">궁금한 모든 것을 알려드립니다.</a></li>
    </ul>
    </div>
    </div>
    </li>
    <li class="d1-4"><a href="/www/kor/story/history.do">맥도날드 이야기</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2">
    <li><a href="/www/kor/story/history.do">맥도날드의 역사</a></li>
    <li><a href="/www/kor/story/promise.do">맥도날드의 약속</a></li>
    <!-- <li><a href="/www/kor/story/q_campaign.do">맥도날드의 품질</a></li> -->
    <li><a href="/www/kor/story/eco.do">맥도날드의 환경이야기</a></li>
    <li><a href="/www/kor/story/society.do">맥도날드의 사회공헌</a></li>
    <li><a href="/event/kor/pc/safety.jsp">맥도날드 안전지킴 캠페인</a></li>
    <!-- <li><a href="/event/kor/pc/pyeongchang_2018.jsp">2018 평창 동계올림픽대회</a></li> -->
    <li><a href="/www/kor/board/list.do">새소식</a></li>
    </ul>
    </div>
    </div>
    </li>
    <li class="d1-5"><a href="/www/kor/findus/delivery.do">맥딜리버리</a></li>
    <li class="d1-6"><a href="/www/kor/findus/thru.do">맥드라이브</a></li>
    <li class="d1-7"><a href="/www/kor/recruit/recruit_person.do">인재채용</a>
    <div class="submenu">
    <div class="inner">
    <ul class="d2">
    <li><a href="/www/kor/recruit/recruit_person.do">맥도날드 문화</a></li>
    <li><a href="/www/kor/recruit/recruit_work.do">업무소개</a></li>
    <!-- <li><a href="/www/kor/recruit/recruit_istory.do">i-story</a></li> -->
    <li><a href="/www/kor/recruit/recruit_process.do">성장의 기회</a></li>
    <li><a href="/www/kor/recruit/apply_gate.do">채용공고 및 지원</a></li>
    <li><a href="http://www.mcdonalds-recruit.co.kr/recruit/recruit_confirmation.asp?pMenuCode=1001">결과확인</a></li>
    </ul>
    </div>
    </div>
    </li>
    <!-- <li class="d1-8"><a href="/www/kor/join/partner_success.do">가맹점 모집</a>
                    <div class="submenu">
                        <div class="inner">
                            <ul class="d2">
                                <li><a href="/www/kor/join/partner_success.do">성공요인</a></li>
                                <li><a href="/www/kor/join/partner_setup.do">개설절차 및 조건</a></li>
                                <li><a href="/www/kor/join/partner_case.do">성공 창업스토리</a></li>
                                <li><a href="/www/kor/join/apply_guide1.do">가맹설명회 신청</a></li>
                                <li><a href="/www/kor/join/partner_apply.do">지원서 작성</a></li>
                            </ul>
                        </div>
                    </div>
                </li> -->
    <li class="d1-9"><a href="/www/kor/store/store.do">임차의뢰</a></li>
    <li class="d1-14"><a href="https://voc.mcd.co.kr/MC/HOM/faqMain.jsp">고객문의</a></li>
    <li class="d1-10"><a href="/www/kor/util/search_result.do">검색</a>
    <form action="/www/kor/util/search_result.do" method="post" name="leftShForm1"><!-- onkeypress="return event.keyCode!=13" -->
    <div class="submenu">
    <div class="inner">
    <fieldset>
    <legend>통합검색</legend>
    <input id="sLeftKeyword2" name="sLeftKeyword2" onkeydown="EnterSubmit1();" placeholder="검색어를 입력해주세요" title="검색어를 입력해주세요" type="text"/>
    <a class="btn_search" href="javascript:leftShSubmit1();"><img alt="검색" src="/www/common/images/kor/common/header/btn_submit.gif"/></a>
    </fieldset>
    </div>
    </div>
    </form>
    </li>
    </ul>
    </nav><!-- //GNB -->
    </header><!-- //Header -->
    <div id="container"><!-- container -->
    <section class="findus" id="contents"><!-- contents -->
    <h2 class="skip">매장찾기</h2><!-- [ 2013-11-15 ] 수정 -->
    <div class="conBody district"><!-- conBody : 컨텐츠 내용 Start -->
    <ul class="find_tabmenu">
    <li class="current"><a href="/www/kor/findus/district.do">지역별</a></li>
    <li><a href="/www/kor/findus/subway.do">지하철별</a></li>
    <li class="red"><a href="/www/kor/findus/delivery.do">맥딜리버리</a></li>
    <li class="red"><a href="/www/kor/findus/thru.do">맥드라이브</a></li>
    </ul>
    <a class="btn_print" href="javascript:printBtn();" id="btnPrint"><img alt="인쇄" height="23" src="../../common/images/kor/common/btn/btn_print.gif" width="24"/></a><!-- [ 2013-11-15 ] 인쇄 버튼 위치 이동 -->
    <h3 class="skip">지역별 검색</h3><!-- [ 2013-11-15 ] 추가 -->
    <div class="searchArea">
    <form action="/www/kor/findus/district.do" method="get" name="shForm">
    <input id="sSearch_yn" name="sSearch_yn" type="hidden" value="Y"/>
    <table class="tbl-findus">
    <caption>매장찾기 지역별 검색 시 지역선택, 매장검색, 이용가능 서비스 정보</caption><!-- [ 2013-11-15 ] 수정 -->
    <colgroup>
    <col style="width:61px;"/>
    <col style="width:360px;"/>
    <col style="width:120px;"/>
    <col/>
    </colgroup>
    <tr>
    <th scope="row"><input id="skey_st" name="skey" type="hidden" value="2"/>매장검색</th>
    <td><input class="type-text" id="skeyword" name="skeyword" onkeydown="EnterSubmitLocal();" title="매장명, 동명, 도로명 입력" type="text" value="서울"/></td>
    <th rowspan="3" scope="row">이용가능 서비스</th>
    <td rowspan="3">
    <div class="inner"><!-- [ 2013-11-25 ] 수정 -->
    <input id="sflag1" name="sflag1" type="checkbox" value="-1-"/><label for="sflag1">24시간</label>
    <input id="sflag2" name="sflag2" type="checkbox" value="-2-"/><label for="sflag2">맥모닝</label>
    </div>
    <div class="inner">
    <input id="sflag3" name="sflag3" type="checkbox" value="-7-"/><label for="sflag3">맥올데이<i class="icon_allday"></i></label>
    <!-- <input type="checkbox" id="sflag3" name="sflag3"  value="-3-" /><label for="sflag3">맥카페</label> -->
    <input id="sflag4" name="sflag4" type="checkbox" value="-4-"/><label for="sflag4">맥딜리버리</label>
    </div>
    <div class="inner">
    <input id="sflag5" name="sflag5" type="checkbox" value="-5-"/><label for="sflag5">맥드라이브<i class="icon_drive"></i></label>
    <input id="sflag6" name="sflag6" type="checkbox" value="-6-"/><label for="sflag6">시그니처 버거<i class="icon_sign"></i></label>
    <!-- [2017-03-13] 수정 -->
    </div>
    </td>
    </tr>
    <tr>
    <th colspan="2" scope="row" style="font-size:0.96em;padding-left:60px;">
    							검색 안내 : 매장명, 동명, 도로명을 검색해 주세요.<br/>
    							검색 예시 : 을지로1가, 창천동 / 남대문로, 연세로 / 서울시청점, 연세대점
    							</th>
    </tr>
    </table>
    <!--  <p class="tip">검색어 또는 조건을 입력 후, 검색 버튼을 클릭!</p> -->
    <div class="btnWrap">
    <span class="btn"><span class="gray big"><a href="/www/kor/findus/district.do">초기화</a></span></span>
    <span class="btn"><span class="red big"><input onclick="shSubmit();" type="button" value="매장찾기"/></span></span>
    </div>
    </form>
    </div>
    <div id="print_div">
    <div class="mapArea"><!-- [ 2013-11-15 ] 수정 -->
    <!-- <p class="address">  (검색지역)</p> -->
    <div class="mapApi" id="map" style="width:887px;height:408px;"></div>
    </div>
    <div class="searchResult">
    <h3 class="skip">지역별 검색 결과</h3><!-- [ 2013-11-15 ] 수정 -->
    <ul class="listHeader clearFix">
    <li>매장명 / 전화번호 / 주소</li>
    <li>영업시간</li>
    <li>맥모닝</li>
    <!-- <li>맥카페</li> -->
    <li>맥올데이</li>
    <li>시그니처 버거</li>
    <li>맥딜리버리</li><!-- [2017-03-13] 수정 -->
    <li>맥드라이브</li><!-- [2017-05-08] 수정 -->
    </ul>
    <ul class="resultList"><!-- [2013-11-25 ]수정 -->
    </ul>
    <div class="paging">
    <a class="btn_first" href="?pageIndex=1&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N"><img alt="처음" src="../../common/images/kor/common/board/btn_first_on.gif"/></a>
    <a class="btn_prev" href="?pageIndex=16&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N"><img alt="이전" src="../../common/images/kor/common/board/btn_prev_on.gif"/></a>
    <a href="?pageIndex=21&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N">21</a>
    <a class="btn_next"><img alt="다음" src="../../common/images/kor/common/board/btn_next_off.gif"/></a>
    <a class="btn_last" href="?pageIndex=21&amp;sSearch_yn=Y&amp;skey=2&amp;skey1=&amp;skey2=&amp;skeyword=서울&amp;skey4=&amp;skey5=&amp;skeyword2=&amp;sflag1=&amp;sflag2=&amp;sflag3=&amp;sflag4=&amp;sflag5=&amp;sflag6=&amp;sflag=N"><img alt="마지막" src="../../common/images/kor/common/board/btn_last_on.gif"/></a>
    </div>
    </div>
    </div>
    </div><!-- conBody : 컨텐츠 내용 End -->
    </section><!-- //contents-->
    <footer class="footWhite" id="footer"><!-- footer -->
    <div class="inner">
    <h2 class="skip">하단영역</h2>
    <div class="sns">
    <div id="fb-root"></div>
    <script>
                            (function(d, s, id) {
                                var js, fjs = d.getElementsByTagName(s)[0];
                                if (d.getElementById(id)) return;
                                js = d.createElement(s); js.id = id;
                                js.src = "//connect.facebook.net/ko_KR/all.js#xfbml=1";
                                fjs.parentNode.insertBefore(js, fjs);
                            }(document, 'script', 'facebook-jssdk'));
                        </script>
    <!-- SNS ICON -->
    <a href="http://www.facebook.com/McDonaldsKorea" id="sns01" onclick="_gaq.push(['_trackEvent', 'PC_SNS_FB', 'click']);" target="_blank"><img alt="페이스북" src="/www/common/images/kor/common/footer/ico_sns01.png"/></a>
    <a href="http://instagram.com/mcdonalds_kr" id="sns02" onclick="_gaq.push(['_trackEvent', 'PC_SNS_INS', 'click']);" target="_blank"><img alt="인스타" src="/www/common/images/kor/common/footer/ico_sns02.png"/></a>
    <a href="http://www.youtube.com/McDonaldsKor" id="sns03" onclick="_gaq.push(['_trackEvent', 'PC_SNS_YTB', 'click']);" target="_blank"><img alt="유튜브" src="/www/common/images/kor/common/footer/ico_sns03.png"/></a>
    <a href="http://story.kakao.com/ch/mcdonalds/feed" id="sns04" onclick="_gaq.push(['_trackEvent', 'PC_SNS_KS', 'click']);" target="_blank"><img alt="카카오스토리" src="/www/common/images/kor/common/footer/ico_sns04.png"/></a>
    <!-- //SNS ICON -->
    <!-- 페북
                        <div class="fb-like" data-href="https://www.facebook.com/McDonaldsKorea" data-layout="button_count" data-action="like" data-show-faces="false" data-share="false"></div>
                        <!-- 인스타
                        <a id="insta" href="http://instagram.com/mcdonalds_kr?ref=badge">
                        	<img src="/www/common/images/kor/common/footer/ico_Insta.png" alt="Instagram" /></a>
                        <!-- 카스 
                        <div id="kakaostory-follow-button" data-id="mcdonalds" data-type="horizontal" data-show-follower-count="true"></div>
                        
                        <!-- 유튜브
                        <a href="http://www.youtube.com/user/McDonaldsKor" class="btn_yTube" target="_blank" title="새창"><img src="/www/common/images/kor/common/btn/btn_youtube.png" width="42" height="20" alt="YouTube" /></a>
                        -->
    <!-- 접근성 -->
    <a class="btn_waMark" href="http://webwatch.or.kr/certification/int_purpose.html" target="_blank" title="새창"><img alt="WA 웹접근성 인증마크" src="/www/common/images/kor/common/footer/waMark.png"/></a>
    </div>
    <div class="footRight">
    <ul class="footMenu">
    <li><a href="https://voc.mcd.co.kr/MC/HOM/faqMain.jsp" onclick="window.open(this.href,'','width=1003px, height=800px'); return false;" target="_blank" title="새창">1:1 문의 및 칭찬</a></li>
    <li><a href="/www/kor/util/private.do"><span class="private_bold">개인정보 취급방침</span></a></li>
    <li><a href="/www/kor/util/sitemap.do">사이트맵</a></li>
    </ul>
    <div class="footInfo">
    <p class="info">한국맥도날드(유) l 대표자: 조주연 l 사업자등록번호: 101-81-26409</p>
    <p class="copy">전화주문 : 1600-5252 ㅣCOPYRIGHT ⓒ 2014 ALL RIGHTS RESERVED BY McDonald's</p>
    <p class="right_txt" style="margin-top:10px; line-height:18px;">당사 홈페이지의 이미지나 내용을 외부로 가져가서 사용하는 행위는 당사의 저작권, 상표권 등 지식재산권을 침해하는 행위입니다.<br/>
                            	무단 공유할 경우 저작권법, 부정경쟁방지법 기타 관련 법령에 따라 책임지게 될 수 있음을 알려 드립니다.<br/>
                            	관련한 질의사항은 고객센터로 문의해 주시기 바랍니다.
                      </p>
    </div>
    </div>
    </div>
    <!-- Google Analytics -->
    <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    
    ga('create', 'UA-15032749-2', 'auto');  // Replace with your property ID.
    ga('create', 'UA-15032749-4', 'auto', 'clientTracker');
    
    ga('send', 'pageview');
    ga('clientTracker.send', 'pageview');
    
    </script>
    <!-- End Google Analytics -->
    <script type="text/javascript">
    
    /* 20170410_구글 코드 구 버전
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-15032749-2']);
      _gaq.push(['_trackPageview']);
    
      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();
    
    */
    
    /* staging
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-15032749-8']);
    _gaq.push(['_trackPageview']);
    
    (function() {
      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    */
    
    /* 카카오스토리 */
    window.kakaoAsyncInit = function () {
        Kakao.Story.createFollowButton({
          container: '#kakaostory-follow-button'
        });
      };
    
      (function (d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//developers.kakao.com/sdk/js/kakao.story.min.js";
        fjs.parentNode.insertBefore(js, fjs);
      }(document, 'script', 'kakao-js-sdk'));
    /* 카카오스토리 */
    </script>
    </footer><!-- //footer -->
    </div><!-- //container -->
    </div><!-- wrap -->
    </body>
    </html>




```python
tmp = soup.find_all('dl','clearFix')
tmp
```




    []




```python
len(tmp)
```




    0




```python
if len(tmp) is 0:
    print('Nothing')
```

    Nothing
    


```python
for pg in tqdm_notebook(count()):
    if pg==50:
        print(pg, '^^'); sleep(1)
        print('Wow, I got out of the loop !!')
        break
    sleep(1/10); print(pg, end='...')
```


    A Jupyter Widget


    0...1...2...3...4...5...6...7...8...9...10...11...12...13...14...15...16...17...18...19...20...21...22...23...24...25...26...27...28...29...30...31...32...33...34...35...36...37...38...39...40...41...42...43...44...45...46...47...48...49...50 ^^
    Wow, I got out of the loop !!
    
    


```python
nameMCD = []
addMCDolder = []
addMCDnewer = []

html = 'http://www.mcdonalds.co.kr/www/kor/findus/district.do?pageIndex={page}&sSearch_yn=Y&skey=2&skey1=&skey2=&skeyword=%EC%84%9C%EC%9A%B8&skey4=&skey5=&skeyword2=&sflag1=&sflag2=&sflag3=&sflag4=&sflag5=&sflag6=&sflag=N'

for pg in tqdm_notebook(count()):
    page = pg+1
    response = urlopen(html.format(page=page))
    soup = BeautifulSoup(response, "lxml")
    tmp = soup.find_all('dl','clearFix')
    
    if len(tmp) is 0:
        print('crawling is finished !!')
        break
    
    for lenTmp in range(len(tmp)):
        tmp2 = tmp[lenTmp].get_text()
        tmp3 = tmp2.split('\n')
    
        nameMCD.append(tmp3[1].replace(' ', ''))
        addMCDolder.append(tmp3[6])
        addMCDnewer.append(tmp3[8])

    sleep(1/10); 
    print('crawling...%d' % page)
    
```


    A Jupyter Widget


    crawling...1
    crawling...2
    crawling...3
    crawling...4
    crawling...5
    crawling...6
    crawling...7
    crawling...8
    crawling...9
    crawling...10
    crawling...11
    crawling...12
    crawling...13
    crawling...14
    crawling...15
    crawling...16
    crawling...17
    crawling...18
    crawling...19
    crawling...20
    crawling...21
    crawling is finished !!
    


```python
len(nameMCD), len(addMCDolder), len(addMCDnewer)
```




    (101, 101, 101)




```python
nameMCD
```




    ['가락DT점',
     '가산디지털점',
     '가산비지니스센터점',
     '강남2호점',
     '강남구청점',
     '강남삼성DT',
     '강동구청점',
     '고척DT',
     '공덕점',
     '과학기술대점',
     '구로디지탈',
     '구로애경점',
     '구산점',
     '구의역점',
     '굽은다리역DT',
     '노량진점',
     '대학로점',
     '등촌DT점',
     '마리오아울렛점',
     '망원점',
     '명동2호점',
     '명동점',
     '명지대점',
     '목동점',
     '미아DT점',
     '미아리점',
     '미아역점',
     '방배점',
     '방학역DT점',
     '보라매',
     '삼선교점',
     '삼성역점',
     '상계DT점',
     '상일동점',
     '서울교대점',
     '서울동묘역점',
     '서울둔촌DT',
     '서울번동DT점',
     '서울상암DMC',
     '서울시청점',
     '서울시흥DT점',
     '서울역점',
     '서초GS점',
     '서초뱅뱅점',
     '석촌역점',
     '선릉점',
     '성균관대점',
     '세이브존노원점',
     '송정역점',
     '송파잠실DT점',
     '수유점',
     '숭실대점',
     '신내점',
     '신도림테크노점',
     '신도림디큐브점',
     '신림점',
     '신사역점',
     '신월DT점',
     '신월SKDT점',
     '신천점',
     '쌍문DT점',
     '안국역점',
     '안암점',
     '압구정CGV점',
     '양재SKDT점',
     '양재점',
     '양천구청DT점',
     '양평SK점',
     '어린이대공원점',
     '여의도점',
     '연세대점',
     '연신내점',
     '염창DT점',
     '영등포점',
     '왕십리점',
     '우장산DT',
     '위례신도시점',
     '이마트상봉점',
     '이마트성수점',
     '이마트은평점',
     '이수점',
     '이태원점',
     '잠실역점',
     '장안사거리점',
     '전농점',
     '종로3가점',
     '종암SK점',
     '중계역점',
     '중계점',
     '중랑점',
     '중앙대점',
     '청담DT점',
     '코엑스',
     '파리공원점',
     '학동역',
     '한국외대점',
     '한양대점',
     '한티점',
     '합정메세나폴리스',
     '홍익대점',
     '홍제역점']




```python
addMCDolder
```




    ['서울특별시 송파구 가락동 193-7',
     '서울특별시 금천구 가산동 50-3 대륭포스트타워6차 1층',
     '서울특별시 금천구 가산동 371-6 가산비지니스센터',
     '서울특별시 강남구 역삼동 822-2 비전타워 2층',
     '서울특별시 강남구 논현동 242-29',
     '서울특별시 강남구 삼성동 113-7',
     '서울특별시 강동구 성내동 539-2',
     '서울특별시 구로구 고척동 73-20',
     '서울특별시 마포구 도화동 559 마포트라팰리스 1층',
     '서울특별시 노원구 공릉동 435-2',
     '서울특별시 구로구 구로동 197-21 태평양물산 1층',
     '서울특별시 구로구 구로동 573 애경백화점',
     '서울특별시 은평구 구산동 1-14',
     '서울특별시 광진구 자양동 216-11',
     '서울특별시 강동구 천호동 31-10',
     '서울특별시 동작구 노량진1동 100-1',
     '서울특별시 종로구 동숭동 1-34',
     '서울특별시 강서구 등촌동 630',
     '서울특별시\xa0금천구 가산동 60-52 마리오 아울렛 1관',
     '서울 마포구 망원동 377-19',
     '서울특별시 중구 회현동3가 1-5',
     '서울특별시 중구 명동1가 48-2 1층',
     '서울특별시 서대문구 남가좌동 324-3',
     '서울특별시 양천구 신정동 899-6',
     '서울특별시 강북구 미아동 682-12',
     '서울특별시 강북구 미아동 71-5',
     '서울특별시 강북구 미아동 197-5',
     '서울특별시 서초구 방배동 909-9',
     '서울특별시 도봉구 도봉동 620-25',
     '서울특별시 영등포구 신길6동 505',
     '서울특별시 성북구 동소문동1가 32-3',
     '서울특별시 강남구 삼성동 158-15',
     '서울특별시 노원구 상계동 1022',
     '서울특별시 강동구 상일동 502, 502-1',
     '서울특별시 서초구 서초동 1674-5',
     '서울특별시 종로구 창신동 290',
     '서울특별시 강동구 둔촌동 517-2',
     '서울특별시 강북구 번동 106',
     '서울특별시 마포구 상암동 1602',
     '서울특별시 중구 을지로1가 32 1층',
     '서울특별시 금천구 시흥동 903-4',
     '서울특별시 용산구 동자동 43-205 서울역 110호',
     '서울특별시 서초구 서초동 1536-1',
     '서울특별시 서초구 서초동 1338-20 현대렉시온 101호',
     '서울특별시 송파구 송파동 84',
     '서울특별시 강남구 역삼동 707-27 I타워 103호',
     '서울특별시 종로구 명륜2가 197-1',
     '서울특별시 노원구 하계동 284 세이브존 1층',
     '서울특별시 강서구 공항동 45-38',
     '서울특별시 송파구 잠실동 305-15',
     '서울특별시 강북구 번동 418-18',
     '서울특별시 동작구 상도동 505-5',
     '서울특별시 중랑구 신내동 666 신아타운 110호',
     '서울특별시 구로구 구로동 3-25 신도림테크노마트',
     '서울특별시 구로구 신도림동 692 디큐브시티 지하2층',
     '서울특별시 관악구 신림동 1641-22',
     '서울특별시 강남구 신사동 514-15',
     '서울특별시 양천구 신월동 199-3',
     '서울특별시 양천구 신월동 525-1',
     '서울특별시 송파구 잠실동 181-9',
     '서울특별시 도봉구 쌍문동 700',
     '서울특별시 종로구 안국동 164',
     '서울특별시 성북구 안암동5가 102-33',
     '서울특별시 강남구 신사동 603-2',
     '서울특별시 서초구 양재동 81',
     '서울특별시 서초구 양재동 24',
     '서울특별시 양천구 신정동 323-20',
     '서울특별시 영등포구 양평동3가 80-2',
     '서울특별시 광진구 화양동 212',
     '서울특별시 영등포구 여의도동 23 IFC Mall B326호',
     '서울특별시 서대문구 창천동 33-12',
     '서울특별시 은평구 갈현동 456-28',
     '서울특별시 강서구 염창동 280-11',
     '서울특별시 영등포구 영등포동3가 10-4',
     '서울특별시 성동구 행당동 286-3',
     '서울시 강서구 화곡동 1026',
     '서울 송파구 장지동 896 위례중앙푸르지오2단지 상가동 119호~122호',
     '서울특별시 중랑구 망우동 506-1',
     '서울특별시 성동구 성수동2가 333-16 이마트 3층 푸드코트내 >> 2,4째주 일요일 휴무',
     '서울특별시 은평구 응암동 90-1 이마트 8층',
     '서울특별시 동작구 사당동 147-29',
     '서울특별시 용산구 이태원동 56-21',
     '서울특별시 송파구 신천동 7-25',
     '서울특별시 동대문구 장안동 308-4',
     '서울특별시 동대문구 전농동 295-96',
     '서울특별시 종로구 종로3가 10',
     '서울특별시 성북구 종암동 10-15',
     '서울특별시 노원구 상계동 763-2',
     '서울특별시 노원구 중계동 359-14',
     '서울특별시 중랑구 상봉동 130-166',
     '서울특별시 동작구 흑석동 221 중앙대학교 약학대학 R&D 센타 지하 1층',
     '서울특별시 강남구 청담동 87-3',
     '서울특별시 강남구 삼성동 159-2',
     '서울특별시 양천구 목동 908-25',
     '서울 강남구 논현동 129-1 1층',
     '서울특별시 동대문구 이문동 305-151',
     '서울특별시 성동구 행당동 31-7',
     '서울특별시 강남구 대치동 938-22',
     '서울특별시 마포구 서교동 490 메세나폴리스 몰동2층',
     '서울특별시 마포구 동교동 162-4 2층',
     '서울특별시 서대문구 홍제동 253-11']




```python
addMCDnewer
```




    ['[도로명주소]서울특별시 송파구 동남로 196 (가락동)',
     '[도로명주소]서울특별시 금천구 벚꽃로 298 (가산동)',
     '[도로명주소]서울특별시 금천구 가산디지털1로 165 (가산동)',
     '[도로명주소]서울특별시 강남구 테헤란로 107, 2층 (역삼동)',
     '[도로명주소]서울특별시 강남구 선릉로 667 (논현동)',
     '[도로명주소]서울특별시 강남구 봉은사로 432',
     '[도로명주소]서울특별시 강동구 성내로 15 (성내동)',
     '[도로명주소]서울특별시 구로구 경인로 393',
     '[도로명주소]서울특별시 마포구 마포대로 53 (도화동)',
     '[도로명주소]서울특별시 노원구 공릉로 231',
     '[도로명주소]서울특별시 구로구 디지털로31길 12 (구로동)',
     '[도로명주소]서울특별시 구로구 구로중앙로 152 (구로동)',
     '[도로명주소]서울특별시 은평구 연서로 131 (구산동)',
     '[도로명주소]서울특별시 광진구 아차산로 376 (자양동)',
     '[도로명주소]서울특별시 강동구 양재대로 1587',
     '[도로명주소]서울특별시 동작구 노량진로 158 (노량진동)',
     '[도로명주소]서울특별시 종로구 대학로 130 (동숭동)',
     '[도로명주소]서울특별시 강서구 양천로 546 (등촌동)',
     '[도로명주소]서울특별시 금천구 디지털로9길 23 (가산동)',
     '[도로명주소]서울 마포구 월드컵로 81',
     '[도로명주소]서울특별시 중구 퇴계로 116-1 (회현동3가)',
     '[도로명주소]서울특별시 중구 명동7길 8 (명동1가)',
     '[도로명주소]서울특별시 서대문구 거북골로 25 (남가좌동)',
     '[도로명주소]서울특별시 양천구 목동로 221 (신정동)',
     '[도로명주소]서울특별시 강북구 미아동 682-12',
     '[도로명주소]서울특별시 강북구 도봉로 48 (미아동)',
     '[도로명주소]서울특별시 강북구 도봉로 204 (미아동)',
     '[도로명주소]서울특별시 서초구 방배로 81 (방배동)',
     '[도로명주소]서울특별시 도봉구 도봉동 620-25',
     '[도로명주소]서울시 영등포구 신길동 505',
     '[도로명주소]서울특별시 성북구 동소문로 13 (동소문동1가)',
     '[도로명주소]서울특별시 강남구 삼성로92길 29 (삼성동)',
     '[도로명주소]서울특별시 노원구 동일로 1612',
     '[도로명주소]서울특별시 강동구 상일로6길 39',
     '[도로명주소]서울특별시 서초구 서초대로 316 (서초동)',
     '[도로명주소]서울특별시 종로구 종로 339',
     '[도로명주소]서울특별시 강동구 양재대로 1382',
     '[도로명주소]서울특별시 강북구 월계로 191',
     '[도로명주소]서울특별시 마포구 월드컵북로 400 1층',
     '[도로명주소]서울특별시 중구 남대문로9길 51 (을지로1가)',
     '[도로명주소]서울특별시 금천구 시흥대로 184',
     '[도로명주소]서울특별시 용산구 한강대로 405 (동자동)',
     '[도로명주소]서울특별시 서초구 효령로49길 52 (서초동)',
     '[도로명주소]서울특별시 서초구 강남대로 305 (서초동)',
     '[도로명주소]서울특별시 송파구 백제고분로 390 (송파동)',
     '[도로명주소]서울특별시 강남구 테헤란로 326 (역삼동)',
     '[도로명주소]서울특별시 종로구 창경궁로 241-1 (명륜2가)',
     '[도로명주소]서울특별시 노원구 한글비석로 57 (하계동)',
     '[도로명주소]서울특별시 강서구 공항대로 21 (공항동)',
     '[도로명주소]서울특별시 송파구 도곡로 434',
     '[도로명주소]서울특별시 강북구 도봉로 342 (번동)',
     '[도로명주소]서울특별시 동작구 사당로 22',
     '[도로명주소]서울특별시 중랑구 봉화산로 194 (신내동)',
     '[도로명주소]서울특별시 구로구 새말로 97 (구로동)',
     '[도로명주소]서울특별시 구로구 경인로 662 (신도림동, 디큐브시티)',
     '[도로명주소]서울특별시 관악구 신림로 310 (신림동)',
     '[도로명주소]서울특별시 강남구 도산대로 123 (신사동)',
     '[도로명주소]서울특별시 양천구 남부순환로 404 (신월동)',
     '[도로명주소]서울특별시 양천구 남부순환로 553 (신월동)',
     '[도로명주소]서울특별시 송파구 올림픽로 108 (잠실동)',
     '[도로명주소]서울특별시 도봉구 도봉로 541 (쌍문동)',
     '[도로명주소]서울특별시 종로구 율곡로 45',
     '[도로명주소]서울특별시 성북구 인촌로24길 42 (안암동5가)',
     '[도로명주소]서울특별시 강남구 논현로 848 (신사동)',
     '[도로명주소]서울특별시 서초구 바우뫼로 178 (양재동)',
     '[도로명주소]서울특별시 서초구 강남대로 213 (양재동)',
     '[도로명주소]서울특별시 양천구 목동동로 71 (신정동)',
     '[도로명주소]서울특별시 영등포구 선유로 195 (양평동3가)',
     '[도로명주소]서울특별시 광진구 광나루로 392 (화양동)',
     '[도로명주소]서울특별시 영등포구 국제금융로 10 (여의도동)',
     '[도로명주소]서울특별시 서대문구 연세로 33 (창천동)',
     '[도로명주소]서울특별시 은평구 연서로 213 (갈현동)',
     '[도로명주소]서울특별시 강서구 공항대로 71길 3 (염창동)',
     '[도로명주소]서울특별시 영등포구 경인로 855 (영등포동3가)',
     '[도로명주소]서울특별시 성동구 왕십리로 321 (행당동)',
     '[도로명주소]서울시 강서구 화곡동 1026',
     '[도로명주소]서울 송파구 위례광장로 290 위례중앙푸르지오2단지 상가동 119호~122호',
     '[도로명주소]서울특별시 중랑구 상봉로 118 (망우동) >> 2,4째주 일요일 휴무',
     '[도로명주소]서울특별시 성동구 뚝섬로 379 (성수동2가) >> 2,4째주 일요일 휴무',
     '[도로명주소]서울특별시 은평구 은평로 111 (응암동) >> 2,4째주 일요일 휴무',
     '[도로명주소]서울특별시 동작구 사당로 300 (사당동)',
     '[도로명주소]서울특별시 용산구 이태원로 142-1',
     '[도로명주소]서울특별시 송파구 송파대로 558 (신천동)',
     '[도로명주소]서울특별시 동대문구 답십리로 291-1 (장안동)',
     '[도로명주소]서울특별시 동대문구 전농로 146 (전농동)',
     '[도로명주소]서울특별시 종로구 종로 115 (종로3가)',
     '[도로명주소]서울특별시 성북구 종암로 58 (종암동)',
     '[도로명주소]서울특별시 노원구 동일로 1341 (상계동)',
     '[도로명주소]서울특별시 노원구 중계로 218 (중계동)',
     '[도로명주소]서울특별시 중랑구 망우로 202 (상봉동)',
     '[도로명주소]서울특별시 동작구 흑석로 84 (흑석동)',
     '[도로명주소]서울특별시 강남구 도산대로 407 (청담동)',
     '[도로명주소]서울특별시 강남구 영동대로 511',
     '[도로명주소]서울특별시 양천구 목동서로 45 (목동)',
     '[도로명주소]서울 강남구 논현로 667',
     '[도로명주소]서울특별시 동대문구 휘경로 15 (이문동)',
     '[도로명주소]서울특별시 성동구 왕십리로 227 (행당동)',
     '[도로명주소]서울특별시 강남구 도곡로 409 (대치동)',
     '[도로명주소]서울특별시 마포구 양화로 45 (서교동, 메세나폴리스)',
     '[도로명주소]서울특별시 마포구 동교동 162-4 2층',
     '[도로명주소]서울특별시 서대문구 통일로 442-1']




```python
addMCDolder[0].split()
```




    ['서울특별시', '송파구', '가락동', '193-7']




```python
addMCDolder[25].split()
```




    ['서울특별시', '강북구', '미아동', '71-5']




```python
addMCDolder[25].split()[1]
```




    '강북구'




```python
guNameMCD = [eachAddress.split()[1] for eachAddress in addMCDolder]
guNameMCD
```




    ['송파구',
     '금천구',
     '금천구',
     '강남구',
     '강남구',
     '강남구',
     '강동구',
     '구로구',
     '마포구',
     '노원구',
     '구로구',
     '구로구',
     '은평구',
     '광진구',
     '강동구',
     '동작구',
     '종로구',
     '강서구',
     '금천구',
     '마포구',
     '중구',
     '중구',
     '서대문구',
     '양천구',
     '강북구',
     '강북구',
     '강북구',
     '서초구',
     '도봉구',
     '영등포구',
     '성북구',
     '강남구',
     '노원구',
     '강동구',
     '서초구',
     '종로구',
     '강동구',
     '강북구',
     '마포구',
     '중구',
     '금천구',
     '용산구',
     '서초구',
     '서초구',
     '송파구',
     '강남구',
     '종로구',
     '노원구',
     '강서구',
     '송파구',
     '강북구',
     '동작구',
     '중랑구',
     '구로구',
     '구로구',
     '관악구',
     '강남구',
     '양천구',
     '양천구',
     '송파구',
     '도봉구',
     '종로구',
     '성북구',
     '강남구',
     '서초구',
     '서초구',
     '양천구',
     '영등포구',
     '광진구',
     '영등포구',
     '서대문구',
     '은평구',
     '강서구',
     '영등포구',
     '성동구',
     '강서구',
     '송파구',
     '중랑구',
     '성동구',
     '은평구',
     '동작구',
     '용산구',
     '송파구',
     '동대문구',
     '동대문구',
     '종로구',
     '성북구',
     '노원구',
     '노원구',
     '중랑구',
     '동작구',
     '강남구',
     '강남구',
     '양천구',
     '강남구',
     '동대문구',
     '성동구',
     '강남구',
     '마포구',
     '마포구',
     '서대문구']




```python
dongNameMCD = [eachAddress.split()[2] for eachAddress in addMCDolder]
dongNameMCD
```




    ['가락동',
     '가산동',
     '가산동',
     '역삼동',
     '논현동',
     '삼성동',
     '성내동',
     '고척동',
     '도화동',
     '공릉동',
     '구로동',
     '구로동',
     '구산동',
     '자양동',
     '천호동',
     '노량진1동',
     '동숭동',
     '등촌동',
     '가산동',
     '망원동',
     '회현동3가',
     '명동1가',
     '남가좌동',
     '신정동',
     '미아동',
     '미아동',
     '미아동',
     '방배동',
     '도봉동',
     '신길6동',
     '동소문동1가',
     '삼성동',
     '상계동',
     '상일동',
     '서초동',
     '창신동',
     '둔촌동',
     '번동',
     '상암동',
     '을지로1가',
     '시흥동',
     '동자동',
     '서초동',
     '서초동',
     '송파동',
     '역삼동',
     '명륜2가',
     '하계동',
     '공항동',
     '잠실동',
     '번동',
     '상도동',
     '신내동',
     '구로동',
     '신도림동',
     '신림동',
     '신사동',
     '신월동',
     '신월동',
     '잠실동',
     '쌍문동',
     '안국동',
     '안암동5가',
     '신사동',
     '양재동',
     '양재동',
     '신정동',
     '양평동3가',
     '화양동',
     '여의도동',
     '창천동',
     '갈현동',
     '염창동',
     '영등포동3가',
     '행당동',
     '화곡동',
     '장지동',
     '망우동',
     '성수동2가',
     '응암동',
     '사당동',
     '이태원동',
     '신천동',
     '장안동',
     '전농동',
     '종로3가',
     '종암동',
     '상계동',
     '중계동',
     '상봉동',
     '흑석동',
     '청담동',
     '삼성동',
     '목동',
     '논현동',
     '이문동',
     '행당동',
     '대치동',
     '서교동',
     '동교동',
     '홍제동']




```python
resultMCD = pd.DataFrame({'MACDONALD_Store':nameMCD, 
                          '구':guNameMCD, 
                          '동':dongNameMCD, 
                          '주소(지번)':addMCDolder, 
                          '주소(도로)':addMCDnewer})

resultMCD.head(10)
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
      <th>MACDONALD_Store</th>
      <th>구</th>
      <th>동</th>
      <th>주소(도로)</th>
      <th>주소(지번)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>가락DT점</td>
      <td>송파구</td>
      <td>가락동</td>
      <td>[도로명주소]서울특별시 송파구 동남로 196 (가락동)</td>
      <td>서울특별시 송파구 가락동 193-7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>가산디지털점</td>
      <td>금천구</td>
      <td>가산동</td>
      <td>[도로명주소]서울특별시 금천구 벚꽃로 298 (가산동)</td>
      <td>서울특별시 금천구 가산동 50-3 대륭포스트타워6차 1층</td>
    </tr>
    <tr>
      <th>2</th>
      <td>가산비지니스센터점</td>
      <td>금천구</td>
      <td>가산동</td>
      <td>[도로명주소]서울특별시 금천구 가산디지털1로 165 (가산동)</td>
      <td>서울특별시 금천구 가산동 371-6 가산비지니스센터</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강남2호점</td>
      <td>강남구</td>
      <td>역삼동</td>
      <td>[도로명주소]서울특별시 강남구 테헤란로 107, 2층 (역삼동)</td>
      <td>서울특별시 강남구 역삼동 822-2 비전타워 2층</td>
    </tr>
    <tr>
      <th>4</th>
      <td>강남구청점</td>
      <td>강남구</td>
      <td>논현동</td>
      <td>[도로명주소]서울특별시 강남구 선릉로 667 (논현동)</td>
      <td>서울특별시 강남구 논현동 242-29</td>
    </tr>
    <tr>
      <th>5</th>
      <td>강남삼성DT</td>
      <td>강남구</td>
      <td>삼성동</td>
      <td>[도로명주소]서울특별시 강남구 봉은사로 432</td>
      <td>서울특별시 강남구 삼성동 113-7</td>
    </tr>
    <tr>
      <th>6</th>
      <td>강동구청점</td>
      <td>강동구</td>
      <td>성내동</td>
      <td>[도로명주소]서울특별시 강동구 성내로 15 (성내동)</td>
      <td>서울특별시 강동구 성내동 539-2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>고척DT</td>
      <td>구로구</td>
      <td>고척동</td>
      <td>[도로명주소]서울특별시 구로구 경인로 393</td>
      <td>서울특별시 구로구 고척동 73-20</td>
    </tr>
    <tr>
      <th>8</th>
      <td>공덕점</td>
      <td>마포구</td>
      <td>도화동</td>
      <td>[도로명주소]서울특별시 마포구 마포대로 53 (도화동)</td>
      <td>서울특별시 마포구 도화동 559 마포트라팰리스 1층</td>
    </tr>
    <tr>
      <th>9</th>
      <td>과학기술대점</td>
      <td>노원구</td>
      <td>공릉동</td>
      <td>[도로명주소]서울특별시 노원구 공릉로 231</td>
      <td>서울특별시 노원구 공릉동 435-2</td>
    </tr>
  </tbody>
</table>
</div>




```python
resultMCD['구'].unique()
```




    array(['송파구', '금천구', '강남구', '강동구', '구로구', '마포구', '노원구', '은평구', '광진구',
           '동작구', '종로구', '강서구', '중구', '서대문구', '양천구', '강북구', '서초구', '도봉구',
           '영등포구', '성북구', '용산구', '중랑구', '관악구', '성동구', '동대문구'], dtype=object)




```python
resultMCD['구'].value_counts()
```




    강남구     11
    서초구      6
    송파구      6
    강북구      5
    마포구      5
    구로구      5
    노원구      5
    양천구      5
    종로구      5
    금천구      4
    동작구      4
    강서구      4
    강동구      4
    영등포구     4
    은평구      3
    성북구      3
    성동구      3
    중랑구      3
    동대문구     3
    중구       3
    서대문구     3
    도봉구      2
    용산구      2
    광진구      2
    관악구      1
    Name: 구, dtype: int64




```python
tmpCounts = resultMCD['구'].value_counts()
tmpCounts.head()
```




    강남구    11
    서초구     6
    송파구     6
    강북구     5
    마포구     5
    Name: 구, dtype: int64




```python
tmpCounts.index
```




    Index(['강남구', '서초구', '송파구', '강북구', '마포구', '구로구', '노원구', '양천구', '종로구', '금천구',
           '동작구', '강서구', '강동구', '영등포구', '은평구', '성북구', '성동구', '중랑구', '동대문구', '중구',
           '서대문구', '도봉구', '용산구', '광진구', '관악구'],
          dtype='object')




```python
# population = pd.read_csv('data/seoul_population.csv', sep=',', encoding='utf-8')
population = pd.read_csv('data/seoul_population.csv', sep=',', encoding='euc-kr')
population.head()
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
      <th>구</th>
      <th>세대</th>
      <th>인구수</th>
      <th>세대당인구</th>
      <th>65세이상고령자</th>
      <th>고령비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>종로구</td>
      <td>73879</td>
      <td>164348</td>
      <td>2.09</td>
      <td>26429</td>
      <td>16.081121</td>
    </tr>
    <tr>
      <th>1</th>
      <td>중구</td>
      <td>60903</td>
      <td>135139</td>
      <td>2.07</td>
      <td>21655</td>
      <td>16.024242</td>
    </tr>
    <tr>
      <th>2</th>
      <td>용산구</td>
      <td>108497</td>
      <td>245411</td>
      <td>2.12</td>
      <td>37238</td>
      <td>15.173729</td>
    </tr>
    <tr>
      <th>3</th>
      <td>성동구</td>
      <td>134543</td>
      <td>314551</td>
      <td>2.28</td>
      <td>41752</td>
      <td>13.273523</td>
    </tr>
    <tr>
      <th>4</th>
      <td>광진구</td>
      <td>161407</td>
      <td>371671</td>
      <td>2.21</td>
      <td>44470</td>
      <td>11.964883</td>
    </tr>
  </tbody>
</table>
</div>




```python
population.set_index('구', inplace=True)
population.head()
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
      <th>세대</th>
      <th>인구수</th>
      <th>세대당인구</th>
      <th>65세이상고령자</th>
      <th>고령비율</th>
    </tr>
    <tr>
      <th>구</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>종로구</th>
      <td>73879</td>
      <td>164348</td>
      <td>2.09</td>
      <td>26429</td>
      <td>16.081121</td>
    </tr>
    <tr>
      <th>중구</th>
      <td>60903</td>
      <td>135139</td>
      <td>2.07</td>
      <td>21655</td>
      <td>16.024242</td>
    </tr>
    <tr>
      <th>용산구</th>
      <td>108497</td>
      <td>245411</td>
      <td>2.12</td>
      <td>37238</td>
      <td>15.173729</td>
    </tr>
    <tr>
      <th>성동구</th>
      <td>134543</td>
      <td>314551</td>
      <td>2.28</td>
      <td>41752</td>
      <td>13.273523</td>
    </tr>
    <tr>
      <th>광진구</th>
      <td>161407</td>
      <td>371671</td>
      <td>2.21</td>
      <td>44470</td>
      <td>11.964883</td>
    </tr>
  </tbody>
</table>
</div>




```python
tmpCounts
```




    강남구     11
    서초구      6
    송파구      6
    강북구      5
    마포구      5
    구로구      5
    노원구      5
    양천구      5
    종로구      5
    금천구      4
    동작구      4
    강서구      4
    강동구      4
    영등포구     4
    은평구      3
    성북구      3
    성동구      3
    중랑구      3
    동대문구     3
    중구       3
    서대문구     3
    도봉구      2
    용산구      2
    광진구      2
    관악구      1
    Name: 구, dtype: int64




```python
# 읽어온 파일에 구별 맥도날드 수 추가
population = pd.concat([population, tmpCounts], axis=1)
population.head()
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
      <th>세대</th>
      <th>인구수</th>
      <th>세대당인구</th>
      <th>65세이상고령자</th>
      <th>고령비율</th>
      <th>구</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>231219</td>
      <td>557865</td>
      <td>2.39</td>
      <td>65859</td>
      <td>11.805544</td>
      <td>11</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>177490</td>
      <td>438225</td>
      <td>2.45</td>
      <td>56983</td>
      <td>13.003138</td>
      <td>4</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>143139</td>
      <td>327511</td>
      <td>2.26</td>
      <td>57002</td>
      <td>17.404606</td>
      <td>5</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>256042</td>
      <td>608361</td>
      <td>2.35</td>
      <td>77381</td>
      <td>12.719586</td>
      <td>4</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>258536</td>
      <td>522292</td>
      <td>1.95</td>
      <td>70807</td>
      <td>13.556976</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
population.rename(columns = {'구':'맥도널드'}, inplace=True)
```


```python
population.head()
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
      <th>세대</th>
      <th>인구수</th>
      <th>세대당인구</th>
      <th>65세이상고령자</th>
      <th>고령비율</th>
      <th>맥도널드</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>231219</td>
      <td>557865</td>
      <td>2.39</td>
      <td>65859</td>
      <td>11.805544</td>
      <td>11</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>177490</td>
      <td>438225</td>
      <td>2.45</td>
      <td>56983</td>
      <td>13.003138</td>
      <td>4</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>143139</td>
      <td>327511</td>
      <td>2.26</td>
      <td>57002</td>
      <td>17.404606</td>
      <td>5</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>256042</td>
      <td>608361</td>
      <td>2.35</td>
      <td>77381</td>
      <td>12.719586</td>
      <td>4</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>258536</td>
      <td>522292</td>
      <td>1.95</td>
      <td>70807</td>
      <td>13.556976</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
population['맥도널드'] / population['인구수'] * 100 * 10000
```




    강남구     19.718032
    강동구      9.127731
    강북구     15.266663
    강서구      6.575043
    관악구      1.914638
    광진구      5.381103
    구로구     11.353418
    금천구     15.788809
    노원구      8.995993
    도봉구      5.796413
    동대문구     8.220034
    동작구      9.834897
    마포구     12.965998
    서대문구     9.234435
    서초구     13.478179
    성동구      9.537404
    성북구      6.609356
    송파구      8.928651
    양천구     10.568881
    영등포구     9.901284
    용산구      8.149594
    은평구      6.119289
    종로구     30.423248
    중구      22.199365
    중랑구      7.289480
    dtype: float64




```python
population['맥버거비율'] = population['맥도널드'] / population['인구수'] * 100 * 10000
```


```python
population.head()
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
      <th>세대</th>
      <th>인구수</th>
      <th>세대당인구</th>
      <th>65세이상고령자</th>
      <th>고령비율</th>
      <th>맥도널드</th>
      <th>맥버거비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>231219</td>
      <td>557865</td>
      <td>2.39</td>
      <td>65859</td>
      <td>11.805544</td>
      <td>11</td>
      <td>19.718032</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>177490</td>
      <td>438225</td>
      <td>2.45</td>
      <td>56983</td>
      <td>13.003138</td>
      <td>4</td>
      <td>9.127731</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>143139</td>
      <td>327511</td>
      <td>2.26</td>
      <td>57002</td>
      <td>17.404606</td>
      <td>5</td>
      <td>15.266663</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>256042</td>
      <td>608361</td>
      <td>2.35</td>
      <td>77381</td>
      <td>12.719586</td>
      <td>4</td>
      <td>6.575043</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>258536</td>
      <td>522292</td>
      <td>1.95</td>
      <td>70807</td>
      <td>13.556976</td>
      <td>1</td>
      <td>1.914638</td>
    </tr>
  </tbody>
</table>
</div>




```python
population.sort_values(by='맥도널드', ascending=False).head(5)
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
      <th>세대</th>
      <th>인구수</th>
      <th>세대당인구</th>
      <th>65세이상고령자</th>
      <th>고령비율</th>
      <th>맥도널드</th>
      <th>맥버거비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>231219</td>
      <td>557865</td>
      <td>2.39</td>
      <td>65859</td>
      <td>11.805544</td>
      <td>11</td>
      <td>19.718032</td>
    </tr>
    <tr>
      <th>송파구</th>
      <td>266550</td>
      <td>671994</td>
      <td>2.50</td>
      <td>77978</td>
      <td>11.603973</td>
      <td>6</td>
      <td>8.928651</td>
    </tr>
    <tr>
      <th>서초구</th>
      <td>174225</td>
      <td>445164</td>
      <td>2.53</td>
      <td>54055</td>
      <td>12.142716</td>
      <td>6</td>
      <td>13.478179</td>
    </tr>
    <tr>
      <th>노원구</th>
      <td>217999</td>
      <td>555803</td>
      <td>2.53</td>
      <td>75081</td>
      <td>13.508563</td>
      <td>5</td>
      <td>8.995993</td>
    </tr>
    <tr>
      <th>종로구</th>
      <td>73879</td>
      <td>164348</td>
      <td>2.09</td>
      <td>26429</td>
      <td>16.081121</td>
      <td>5</td>
      <td>30.423248</td>
    </tr>
  </tbody>
</table>
</div>




```python
population.sort_values(by='인구수', ascending=False).head(5)
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
      <th>세대</th>
      <th>인구수</th>
      <th>세대당인구</th>
      <th>65세이상고령자</th>
      <th>고령비율</th>
      <th>맥도널드</th>
      <th>맥버거비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>송파구</th>
      <td>266550</td>
      <td>671994</td>
      <td>2.50</td>
      <td>77978</td>
      <td>11.603973</td>
      <td>6</td>
      <td>8.928651</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>256042</td>
      <td>608361</td>
      <td>2.35</td>
      <td>77381</td>
      <td>12.719586</td>
      <td>4</td>
      <td>6.575043</td>
    </tr>
    <tr>
      <th>강남구</th>
      <td>231219</td>
      <td>557865</td>
      <td>2.39</td>
      <td>65859</td>
      <td>11.805544</td>
      <td>11</td>
      <td>19.718032</td>
    </tr>
    <tr>
      <th>노원구</th>
      <td>217999</td>
      <td>555803</td>
      <td>2.53</td>
      <td>75081</td>
      <td>13.508563</td>
      <td>5</td>
      <td>8.995993</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>258536</td>
      <td>522292</td>
      <td>1.95</td>
      <td>70807</td>
      <td>13.556976</td>
      <td>1</td>
      <td>1.914638</td>
    </tr>
  </tbody>
</table>
</div>




```python
population.sort_values(by='맥버거비율', ascending=False).head(5)
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
      <th>세대</th>
      <th>인구수</th>
      <th>세대당인구</th>
      <th>65세이상고령자</th>
      <th>고령비율</th>
      <th>맥도널드</th>
      <th>맥버거비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>종로구</th>
      <td>73879</td>
      <td>164348</td>
      <td>2.09</td>
      <td>26429</td>
      <td>16.081121</td>
      <td>5</td>
      <td>30.423248</td>
    </tr>
    <tr>
      <th>중구</th>
      <td>60903</td>
      <td>135139</td>
      <td>2.07</td>
      <td>21655</td>
      <td>16.024242</td>
      <td>3</td>
      <td>22.199365</td>
    </tr>
    <tr>
      <th>강남구</th>
      <td>231219</td>
      <td>557865</td>
      <td>2.39</td>
      <td>65859</td>
      <td>11.805544</td>
      <td>11</td>
      <td>19.718032</td>
    </tr>
    <tr>
      <th>금천구</th>
      <td>106333</td>
      <td>253344</td>
      <td>2.20</td>
      <td>34640</td>
      <td>13.673109</td>
      <td>4</td>
      <td>15.788809</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>143139</td>
      <td>327511</td>
      <td>2.26</td>
      <td>57002</td>
      <td>17.404606</td>
      <td>5</td>
      <td>15.266663</td>
    </tr>
  </tbody>
</table>
</div>




```python
import json
import folium
import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)

geo_path = 'data/skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

macDat = pd.DataFrame({'gu':population.index, 'counts':population['맥버거비율']})

map = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='Stamen Toner')

map.choropleth(geo_str,
              data=macDat,
              columns=['gu', 'counts'],
              fill_color='PuRd', #PuRd, YlGnBu
              key_on='feature.id')
```


```python
map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC5taW4uY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiIC8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2dpdC5jb20vcHl0aG9uLXZpc3VhbGl6YXRpb24vZm9saXVtL21hc3Rlci9mb2xpdW0vdGVtcGxhdGVzL2xlYWZsZXQuYXdlc29tZS5yb3RhdGUuY3NzIiAvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfYjk2ZmM3ZTUyZWRjNGUwNWIwM2FjYTAyMDEyZDgxODAgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL2QzLzMuNS41L2QzLm1pbi5qcyI+PC9zY3JpcHQ+CjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfYjk2ZmM3ZTUyZWRjNGUwNWIwM2FjYTAyMDEyZDgxODAiID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgYm91bmRzID0gbnVsbDsKICAgICAgICAgICAgCgogICAgICAgICAgICB2YXIgbWFwX2I5NmZjN2U1MmVkYzRlMDViMDNhY2EwMjAxMmQ4MTgwID0gTC5tYXAoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbWFwX2I5NmZjN2U1MmVkYzRlMDViMDNhY2EwMjAxMmQ4MTgwJywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHtjZW50ZXI6IFszNy41NTAyLDEyNi45ODJdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTEsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyX2Q0YzdjNGVlOWJhMDQxYjI5YmQ4MjM5NzhhNGE1YmZiID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly9zdGFtZW4tdGlsZXMte3N9LmEuc3NsLmZhc3RseS5uZXQvdG9uZXIve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAiYXR0cmlidXRpb24iOiBudWxsLAogICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwKICAibWF4Wm9vbSI6IDE4LAogICJtaW5ab29tIjogMSwKICAibm9XcmFwIjogZmFsc2UsCiAgInN1YmRvbWFpbnMiOiAiYWJjIgp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9iOTZmYzdlNTJlZGM0ZTA1YjAzYWNhMDIwMTJkODE4MCk7CiAgICAgICAgCiAgICAKCiAgICAgICAgICAgIAoKICAgICAgICAgICAgICAgIHZhciBnZW9fanNvbl9kNDU4ZWIzN2Y1Yzc0NjJlOTUwMDRkMjhhZTk5ZTllYSA9IEwuZ2VvSnNvbigKICAgICAgICAgICAgICAgICAgICB7ImZlYXR1cmVzIjogW3siZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjExNTE5NTg0OTgxNjA2LCAzNy41NTc1MzMxODA3MDQ5MTVdLCBbMTI3LjE2NjgzMTg0MzY2MTI5LCAzNy41NzY3MjQ4NzM4ODYyN10sIFsxMjcuMTg0MDg3OTIzMzAxNTIsIDM3LjU1ODE0MjgwMzY5NTc1XSwgWzEyNy4xNjUzMDk4NDMwNzQ0NywgMzcuNTQyMjE4NTEyNTg2OTNdLCBbMTI3LjE0NjcyODA2ODIzNTAyLCAzNy41MTQxNTY4MDY4MDI5MV0sIFsxMjcuMTIxMjMxNjU3MTk2MTUsIDM3LjUyNTI4MjcwMDg5XSwgWzEyNy4xMTE2NzY0MjAzNjA4LCAzNy41NDA2Njk5NTUzMjQ5NjVdLCBbMTI3LjExNTE5NTg0OTgxNjA2LCAzNy41NTc1MzMxODA3MDQ5MTVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWMxNVx1YjNkOVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMjUwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFjMTVcdWIzZDlcdWFkNmMiLCAibmFtZV9lbmciOiAiR2FuZ2RvbmctZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjYzk5NGM3IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDY5MDY5ODEzMDM3MiwgMzcuNTIyMjc5NDIzNTA1MDI2XSwgWzEyNy4xMDA4NzUxOTc5MTk2MiwgMzcuNTI0ODQxMjIwMTY3MDU1XSwgWzEyNy4xMTE2NzY0MjAzNjA4LCAzNy41NDA2Njk5NTUzMjQ5NjVdLCBbMTI3LjEyMTIzMTY1NzE5NjE1LCAzNy41MjUyODI3MDA4OV0sIFsxMjcuMTQ2NzI4MDY4MjM1MDIsIDM3LjUxNDE1NjgwNjgwMjkxXSwgWzEyNy4xNjM0OTQ0MjE1NzY1LCAzNy40OTc0NDU0MDYwOTc0ODRdLCBbMTI3LjE0MjA2MDU4NDEzMjc0LCAzNy40NzA4OTgxOTA5ODUwMV0sIFsxMjcuMTI0NDA1NzEwODA4OTMsIDM3LjQ2MjQwNDQ1NTg3MDQ4XSwgWzEyNy4xMTExNzA4NTIwMTIzOCwgMzcuNDg1NzA4MzgxNTEyNDQ1XSwgWzEyNy4wNzE5MTQ2MDAwNzI0LCAzNy41MDIyNDAxMzU4NzY2OV0sIFsxMjcuMDY5MDY5ODEzMDM3MiwgMzcuNTIyMjc5NDIzNTA1MDI2XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWMxYTFcdWQzMGNcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTI0MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjMWExXHVkMzBjXHVhZDZjIiwgIm5hbWVfZW5nIjogIlNvbmdwYS1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNjOTk0YzciLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wNTg2NzM1OTI4ODM5OCwgMzcuNTI2Mjk5NzQ5MjI1NjhdLCBbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl0sIFsxMjcuMDcxOTE0NjAwMDcyNCwgMzcuNTAyMjQwMTM1ODc2NjldLCBbMTI3LjExMTE3MDg1MjAxMjM4LCAzNy40ODU3MDgzODE1MTI0NDVdLCBbMTI3LjEyNDQwNTcxMDgwODkzLCAzNy40NjI0MDQ0NTU4NzA0OF0sIFsxMjcuMDk4NDI3NTkzMTg3NTEsIDM3LjQ1ODYyMjUzODU3NDYxXSwgWzEyNy4wODY0MDQ0MDU3ODE1NiwgMzcuNDcyNjk3OTM1MTg0NjU1XSwgWzEyNy4wNTU5MTcwNDgxOTA0LCAzNy40NjU5MjI4OTE0MDc3XSwgWzEyNy4wMzYyMTkxNTA5ODc5OCwgMzcuNDgxNzU4MDI0Mjc2MDNdLCBbMTI3LjAxMzk3MTE5NjY3NTEzLCAzNy41MjUwMzk4ODI4OTY2OV0sIFsxMjcuMDIzMDI4MzE4OTA1NTksIDM3LjUzMjMxODk5NTgyNjYzXSwgWzEyNy4wNTg2NzM1OTI4ODM5OCwgMzcuNTI2Mjk5NzQ5MjI1NjhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWMxNVx1YjBhOFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMjMwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFjMTVcdWIwYThcdWFkNmMiLCAibmFtZV9lbmciOiAiR2FuZ25hbS1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNlNzI5OGEiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldLCBbMTI3LjAzNjIxOTE1MDk4Nzk4LCAzNy40ODE3NTgwMjQyNzYwM10sIFsxMjcuMDU1OTE3MDQ4MTkwNCwgMzcuNDY1OTIyODkxNDA3N10sIFsxMjcuMDg2NDA0NDA1NzgxNTYsIDM3LjQ3MjY5NzkzNTE4NDY1NV0sIFsxMjcuMDk4NDI3NTkzMTg3NTEsIDM3LjQ1ODYyMjUzODU3NDYxXSwgWzEyNy4wOTA0NjkyODU2NTk1MSwgMzcuNDQyOTY4MjYxMTQxODVdLCBbMTI3LjA2Nzc4MTA3NjA1NDMzLCAzNy40MjYxOTc0MjQwNTczMTRdLCBbMTI3LjA0OTU3MjMyOTg3MTQyLCAzNy40MjgwNTgzNjg0NTY5NF0sIFsxMjcuMDM4ODE3ODI1OTc5MjIsIDM3LjQ1MzgyMDM5ODUxNzE1XSwgWzEyNi45OTA3MjA3MzE5NTQ2MiwgMzcuNDU1MzI2MTQzMzEwMDI1XSwgWzEyNi45ODM2NzY2ODI5MTgwMiwgMzcuNDczODU2NDkyNjkyMDg2XSwgWzEyNi45ODIyMzgwNzkxNjA4MSwgMzcuNTA5MzE0OTY2NzcwMzI2XSwgWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzExY1x1Y2QwOFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMjIwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWMxMWNcdWNkMDhcdWFkNmMiLCAibmFtZV9lbmciOiAiU2VvY2hvLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2RmNjViMCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk4MzY3NjY4MjkxODAyLCAzNy40NzM4NTY0OTI2OTIwODZdLCBbMTI2Ljk5MDcyMDczMTk1NDYyLCAzNy40NTUzMjYxNDMzMTAwMjVdLCBbMTI2Ljk2NTIwNDM5MDg1MTQzLCAzNy40MzgyNDk3ODQwMDYyNDZdLCBbMTI2Ljk1MDAwMDAxMDEwMTgyLCAzNy40MzYxMzQ1MTE2NTcxOV0sIFsxMjYuOTMwODQ0MDgwNTY1MjUsIDM3LjQ0NzM4MjkyODMzMzk5NF0sIFsxMjYuOTE2NzcyODE0NjYwMSwgMzcuNDU0OTA1NjY0MjM3ODldLCBbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV0sIFsxMjYuOTA1MzE5NzU4MDE4MTIsIDM3LjQ4MjE4MDg3NTc1NDI5XSwgWzEyNi45NDkyMjY2MTM4OTUwOCwgMzcuNDkxMjU0Mzc0OTU2NDldLCBbMTI2Ljk3MjU4OTE4NTA2NjIsIDM3LjQ3MjU2MTM2MzI3ODEyNV0sIFsxMjYuOTgzNjc2NjgyOTE4MDIsIDM3LjQ3Mzg1NjQ5MjY5MjA4Nl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZDAwXHVjNTQ1XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEyMTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWQwMFx1YzU0NVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJHd2FuYWstZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZDRiOWRhIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuOTgyMjM4MDc5MTYwODEsIDM3LjUwOTMxNDk2Njc3MDMyNl0sIFsxMjYuOTgzNjc2NjgyOTE4MDIsIDM3LjQ3Mzg1NjQ5MjY5MjA4Nl0sIFsxMjYuOTcyNTg5MTg1MDY2MiwgMzcuNDcyNTYxMzYzMjc4MTI1XSwgWzEyNi45NDkyMjY2MTM4OTUwOCwgMzcuNDkxMjU0Mzc0OTU2NDldLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuOTIxNzc4OTMxNzQ4MjUsIDM3LjQ5NDg4OTg3NzQxNTE3Nl0sIFsxMjYuOTI4MTA2Mjg4MjgyNzksIDM3LjUxMzI5NTk1NzMyMDE1XSwgWzEyNi45NTI0OTk5MDI5ODE1OSwgMzcuNTE3MjI1MDA3NDE4MTNdLCBbMTI2Ljk4MjIzODA3OTE2MDgxLCAzNy41MDkzMTQ5NjY3NzAzMjZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YjNkOVx1Yzc5MVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMjAwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWIzZDlcdWM3OTFcdWFkNmMiLCAibmFtZV9lbmciOiAiRG9uZ2phay1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNjOTk0YzciLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi44OTE4NDY2Mzg2Mjc2NCwgMzcuNTQ3MzczOTc0OTk3MTE0XSwgWzEyNi45NDU2NjczMzA4MzIxMiwgMzcuNTI2NjE3NTQyNDUzMzY2XSwgWzEyNi45NTI0OTk5MDI5ODE1OSwgMzcuNTE3MjI1MDA3NDE4MTNdLCBbMTI2LjkyODEwNjI4ODI4Mjc5LCAzNy41MTMyOTU5NTczMjAxNV0sIFsxMjYuOTIxNzc4OTMxNzQ4MjUsIDM3LjQ5NDg4OTg3NzQxNTE3Nl0sIFsxMjYuOTA1MzE5NzU4MDE4MTIsIDM3LjQ4MjE4MDg3NTc1NDI5XSwgWzEyNi44OTU5NDc3Njc4MjQ4NSwgMzcuNTA0Njc1MjgxMzA5MTc2XSwgWzEyNi44ODE1NjQwMjM1Mzg2MiwgMzcuNTEzOTcwMDM0NzY1Njg0XSwgWzEyNi44ODgyNTc1Nzg2MDA5OSwgMzcuNTQwNzk3MzM2MzAyMzJdLCBbMTI2Ljg5MTg0NjYzODYyNzY0LCAzNy41NDczNzM5NzQ5OTcxMTRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzYwMVx1YjRmMVx1ZDNlY1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTkwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM2MDFcdWI0ZjFcdWQzZWNcdWFkNmMiLCAibmFtZV9lbmciOiAiWWVvbmdkZXVuZ3BvLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M5OTRjNyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV0sIFsxMjYuOTE2NzcyODE0NjYwMSwgMzcuNDU0OTA1NjY0MjM3ODldLCBbMTI2LjkzMDg0NDA4MDU2NTI1LCAzNy40NDczODI5MjgzMzM5OTRdLCBbMTI2LjkwMjU4MzE3MTE2OTcsIDM3LjQzNDU0OTM2NjM0OTEyNF0sIFsxMjYuODc2ODMyNzE1MDI0MjgsIDM3LjQ4MjU3NjU5MTYwNzMwNV0sIFsxMjYuOTAxNTYwOTQxMjk4OTUsIDM3LjQ3NzUzODQyNzg5OTAxXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFlMDhcdWNjOWNcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTE4MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhZTA4XHVjYzljXHVhZDZjIiwgIm5hbWVfZW5nIjogIkdldW1jaGVvbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNkZjY1YjAiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi44MjY4ODA4MTUxNzMxNCwgMzcuNTA1NDg5NzIyMzI4OTZdLCBbMTI2Ljg4MTU2NDAyMzUzODYyLCAzNy41MTM5NzAwMzQ3NjU2ODRdLCBbMTI2Ljg5NTk0Nzc2NzgyNDg1LCAzNy41MDQ2NzUyODEzMDkxNzZdLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuOTAxNTYwOTQxMjk4OTUsIDM3LjQ3NzUzODQyNzg5OTAxXSwgWzEyNi44NzY4MzI3MTUwMjQyOCwgMzcuNDgyNTc2NTkxNjA3MzA1XSwgWzEyNi44NDc2MjY3NjA1NDk1MywgMzcuNDcxNDY3MjM5MzYzMjNdLCBbMTI2LjgzNTQ5NDg1MDc2MTk2LCAzNy40NzQwOTgyMzY5NzUwOTVdLCBbMTI2LjgyMjY0Nzk2NzkxMzQ4LCAzNy40ODc4NDc2NDkyMTQ3XSwgWzEyNi44MjUwNDczNjMzMTQwNiwgMzcuNTAzMDI2MTI2NDA0NDNdLCBbMTI2LjgyNjg4MDgxNTE3MzE0LCAzNy41MDU0ODk3MjIzMjg5Nl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZDZjXHViODVjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExNzAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWQ2Y1x1Yjg1Y1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJHdXJvLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2RmNjViMCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljc5NTc1NzY4NTUyOTA3LCAzNy41Nzg4MTA4NzYzMzIwMl0sIFsxMjYuODA3MDIxMTUwMjM1OTcsIDM3LjYwMTIzMDAxMDEzMjI4XSwgWzEyNi44MjI1MTQzODQ3NzEwNSwgMzcuNTg4MDQzMDgxMDA4Ml0sIFsxMjYuODU5ODQxOTkzOTk2NjcsIDM3LjU3MTg0Nzg1NTI5Mjc0NV0sIFsxMjYuODkxODQ2NjM4NjI3NjQsIDM3LjU0NzM3Mzk3NDk5NzExNF0sIFsxMjYuODg4MjU3NTc4NjAwOTksIDM3LjU0MDc5NzMzNjMwMjMyXSwgWzEyNi44NjYzNzQ2NDMyMTIzOCwgMzcuNTQ4NTkxOTEwOTQ4MjNdLCBbMTI2Ljg2NjEwMDczNDc2Mzk1LCAzNy41MjY5OTk2NDE0NDY2OV0sIFsxMjYuODQyNTcyOTE5NDMxNTMsIDM3LjUyMzczNzA3ODA1NTk2XSwgWzEyNi44MjQyMzMxNDI2NzIyLCAzNy41Mzc4ODA3ODc1MzI0OF0sIFsxMjYuNzczMjQ0MTc3MTc3MDMsIDM3LjU0NTkxMjM0NTA1NTRdLCBbMTI2Ljc2OTc5MTgwNTc5MzUyLCAzNy41NTEzOTE4MzAwODgwOV0sIFsxMjYuNzk1NzU3Njg1NTI5MDcsIDM3LjU3ODgxMDg3NjMzMjAyXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFjMTVcdWMxMWNcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTE2MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhYzE1XHVjMTFjXHVhZDZjIiwgIm5hbWVfZW5nIjogIkdhbmdzZW8tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjYzk5NGM3IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuODI0MjMzMTQyNjcyMiwgMzcuNTM3ODgwNzg3NTMyNDhdLCBbMTI2Ljg0MjU3MjkxOTQzMTUzLCAzNy41MjM3MzcwNzgwNTU5Nl0sIFsxMjYuODY2MTAwNzM0NzYzOTUsIDM3LjUyNjk5OTY0MTQ0NjY5XSwgWzEyNi44NjYzNzQ2NDMyMTIzOCwgMzcuNTQ4NTkxOTEwOTQ4MjNdLCBbMTI2Ljg4ODI1NzU3ODYwMDk5LCAzNy41NDA3OTczMzYzMDIzMl0sIFsxMjYuODgxNTY0MDIzNTM4NjIsIDM3LjUxMzk3MDAzNDc2NTY4NF0sIFsxMjYuODI2ODgwODE1MTczMTQsIDM3LjUwNTQ4OTcyMjMyODk2XSwgWzEyNi44MjQyMzMxNDI2NzIyLCAzNy41Mzc4ODA3ODc1MzI0OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjNTkxXHVjYzljXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExNTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzU5MVx1Y2M5Y1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJZYW5nY2hlb24tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjYzk5NGM3IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuOTA1MjIwNjU4MzEwNTMsIDM3LjU3NDA5NzAwNTIyNTc0XSwgWzEyNi45Mzg5ODE2MTc5ODk3MywgMzcuNTUyMzEwMDAzNzI4MTI0XSwgWzEyNi45NjM1ODIyNjcxMDgxMiwgMzcuNTU2MDU2MzU0NzUxNTRdLCBbMTI2Ljk2NDQ4NTcwNTUzMDU1LCAzNy41NDg3MDU2OTIwMjE2MzVdLCBbMTI2Ljk0NTY2NzMzMDgzMjEyLCAzNy41MjY2MTc1NDI0NTMzNjZdLCBbMTI2Ljg5MTg0NjYzODYyNzY0LCAzNy41NDczNzM5NzQ5OTcxMTRdLCBbMTI2Ljg1OTg0MTk5Mzk5NjY3LCAzNy41NzE4NDc4NTUyOTI3NDVdLCBbMTI2Ljg4NDMzMjg0NzczMjg4LCAzNy41ODgxNDMzMjI4ODA1MjZdLCBbMTI2LjkwNTIyMDY1ODMxMDUzLCAzNy41NzQwOTcwMDUyMjU3NF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHViOWM4XHVkM2VjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExNDAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YjljOFx1ZDNlY1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJNYXBvLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2RmNjViMCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk1MjQ3NTIwMzA1NzIsIDM3LjYwNTA4NjkyNzM3MDQ1XSwgWzEyNi45NTU2NTQyNTg0NjQ2MywgMzcuNTc2MDgwNzkwODgxNDU2XSwgWzEyNi45Njg3MzYzMzI3OTA3NSwgMzcuNTYzMTM2MDQ2OTA4MjddLCBbMTI2Ljk2MzU4MjI2NzEwODEyLCAzNy41NTYwNTYzNTQ3NTE1NF0sIFsxMjYuOTM4OTgxNjE3OTg5NzMsIDM3LjU1MjMxMDAwMzcyODEyNF0sIFsxMjYuOTA1MjIwNjU4MzEwNTMsIDM3LjU3NDA5NzAwNTIyNTc0XSwgWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMTFjXHViMzAwXHViYjM4XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExMzAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzExY1x1YjMwMFx1YmIzOFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJTZW9kYWVtdW4tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjYzk5NGM3IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuOTczODg2NDEyODcwMiwgMzcuNjI5NDk2MzQ3ODY4ODhdLCBbMTI2Ljk1NDI3MDE3MDA2MTI5LCAzNy42MjIwMzM0MzEzMzk0MjVdLCBbMTI2Ljk1MjQ3NTIwMzA1NzIsIDM3LjYwNTA4NjkyNzM3MDQ1XSwgWzEyNi45MDUyMjA2NTgzMTA1MywgMzcuNTc0MDk3MDA1MjI1NzRdLCBbMTI2Ljg4NDMzMjg0NzczMjg4LCAzNy41ODgxNDMzMjI4ODA1MjZdLCBbMTI2LjkwMzk2NjgxMDAzNTk1LCAzNy41OTIyNzQwMzQxOTk0Ml0sIFsxMjYuOTAzMDMwNjYxNzc2NjgsIDM3LjYwOTk3NzkxMTQwMTM0NF0sIFsxMjYuOTE0NTU0ODE0Mjk2NDgsIDM3LjY0MTUwMDUwOTk2OTM1XSwgWzEyNi45NTY0NzM3OTczODcsIDM3LjY1MjQ4MDczNzMzOTQ0NV0sIFsxMjYuOTczODg2NDEyODcwMiwgMzcuNjI5NDk2MzQ3ODY4ODhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1Yzc0MFx1ZDNjOVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTIwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM3NDBcdWQzYzlcdWFkNmMiLCAibmFtZV9lbmciOiAiRXVucHllb25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2Q0YjlkYSIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA4Mzg3NTI3MDMxOTUsIDM3LjY5MzU5NTM0MjAyMDM0XSwgWzEyNy4wOTcwNjM5MTMwOTY5NSwgMzcuNjg2MzgzNzE5MzcyMjk0XSwgWzEyNy4wOTQ0MDc2NjI5ODcxNywgMzcuNjQ3MTM0OTA0NzMwNDVdLCBbMTI3LjExMzI2Nzk1ODU1MTk5LCAzNy42Mzk2MjI5MDUzMTU5MjVdLCBbMTI3LjEwNzgyMjc3Njg4MTI5LCAzNy42MTgwNDI0NDI0MTA2OV0sIFsxMjcuMDczNTEyNDM4MjUyNzgsIDM3LjYxMjgzNjYwMzQyMzEzXSwgWzEyNy4wNTIwOTM3MzU2ODYxOSwgMzcuNjIxNjQwNjU0ODc3ODJdLCBbMTI3LjA0MzU4ODAwODk1NjA5LCAzNy42Mjg0ODkzMTI5ODcxNV0sIFsxMjcuMDU4MDAwNzUyMjAwOTEsIDM3LjY0MzE4MjYzODc4Mjc2XSwgWzEyNy4wNTI4ODQ3OTcxMDQ4NSwgMzcuNjg0MjM4NTcwODQzNDddLCBbMTI3LjA4Mzg3NTI3MDMxOTUsIDM3LjY5MzU5NTM0MjAyMDM0XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIxNzhcdWM2ZDBcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTExMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViMTc4XHVjNmQwXHVhZDZjIiwgIm5hbWVfZW5nIjogIk5vd29uLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M5OTRjNyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA1Mjg4NDc5NzEwNDg1LCAzNy42ODQyMzg1NzA4NDM0N10sIFsxMjcuMDU4MDAwNzUyMjAwOTEsIDM3LjY0MzE4MjYzODc4Mjc2XSwgWzEyNy4wNDM1ODgwMDg5NTYwOSwgMzcuNjI4NDg5MzEyOTg3MTVdLCBbMTI3LjAxNDY1OTM1ODkyNDY2LCAzNy42NDk0MzY4NzQ5NjgxMl0sIFsxMjcuMDIwNjIxMTYxNDEzODksIDM3LjY2NzE3MzU3NTk3MTIwNV0sIFsxMjcuMDEwMzk2NjYwNDIwNzEsIDM3LjY4MTg5NDU4OTYwMzU5NF0sIFsxMjcuMDE3OTUwOTkyMDM0MzIsIDM3LjY5ODI0NDEyNzc1NjYyXSwgWzEyNy4wNTI4ODQ3OTcxMDQ4NSwgMzcuNjg0MjM4NTcwODQzNDddXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YjNjNFx1YmQwOVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTAwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWIzYzRcdWJkMDlcdWFkNmMiLCAibmFtZV9lbmciOiAiRG9ib25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2Q0YjlkYSIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk5MzgzOTAzNDI0LCAzNy42NzY2ODE3NjExOTkwODVdLCBbMTI3LjAxMDM5NjY2MDQyMDcxLCAzNy42ODE4OTQ1ODk2MDM1OTRdLCBbMTI3LjAyMDYyMTE2MTQxMzg5LCAzNy42NjcxNzM1NzU5NzEyMDVdLCBbMTI3LjAxNDY1OTM1ODkyNDY2LCAzNy42NDk0MzY4NzQ5NjgxMl0sIFsxMjcuMDQzNTg4MDA4OTU2MDksIDM3LjYyODQ4OTMxMjk4NzE1XSwgWzEyNy4wNTIwOTM3MzU2ODYxOSwgMzcuNjIxNjQwNjU0ODc3ODJdLCBbMTI3LjAzODkyNDAwOTkyMzAxLCAzNy42MDk3MTU2MTEwMjM4MTZdLCBbMTI3LjAxMjgxNTQ3NDk1MjMsIDM3LjYxMzY1MjI0MzQ3MDI1Nl0sIFsxMjYuOTg2NzI3MDU1MTM4NjksIDM3LjYzMzc3NjQxMjg4MTk2XSwgWzEyNi45ODE3NDUyNjc2NTUxLCAzNy42NTIwOTc2OTM4Nzc3Nl0sIFsxMjYuOTkzODM5MDM0MjQsIDM3LjY3NjY4MTc2MTE5OTA4NV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhYzE1XHViZDgxXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwOTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWMxNVx1YmQ4MVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJHYW5nYnVrLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2RmNjViMCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk3NzE3NTQwNjQxNiwgMzcuNjI4NTk3MTU0MDAzODhdLCBbMTI2Ljk4NjcyNzA1NTEzODY5LCAzNy42MzM3NzY0MTI4ODE5Nl0sIFsxMjcuMDEyODE1NDc0OTUyMywgMzcuNjEzNjUyMjQzNDcwMjU2XSwgWzEyNy4wMzg5MjQwMDk5MjMwMSwgMzcuNjA5NzE1NjExMDIzODE2XSwgWzEyNy4wNTIwOTM3MzU2ODYxOSwgMzcuNjIxNjQwNjU0ODc3ODJdLCBbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM10sIFsxMjcuMDczODI3MDcwOTkyMjcsIDM3LjYwNDAxOTI4OTg2NDE5XSwgWzEyNy4wNDI3MDUyMjIwOTQsIDM3LjU5MjM5NDM3NTkzMzkxXSwgWzEyNy4wMjUyNzI1NDUyODAwMywgMzcuNTc1MjQ2MTYyNDUyNDldLCBbMTI2Ljk5MzQ4MjkzMzU4MzE0LCAzNy41ODg1NjU0NTcyMTYxNTZdLCBbMTI2Ljk4ODc5ODY1OTkyMzg0LCAzNy42MTE4OTI3MzE5NzU2XSwgWzEyNi45NzcxNzU0MDY0MTYsIDM3LjYyODU5NzE1NDAwMzg4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWMxMzFcdWJkODFcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTA4MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjMTMxXHViZDgxXHVhZDZjIiwgIm5hbWVfZW5nIjogIlNlb25nYnVrLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M5OTRjNyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM10sIFsxMjcuMTA3ODIyNzc2ODgxMjksIDM3LjYxODA0MjQ0MjQxMDY5XSwgWzEyNy4xMjAxMjQ2MDIwMTE0LCAzNy42MDE3ODQ1NzU5ODE4OF0sIFsxMjcuMTAzMDQxNzQyNDkyMTQsIDM3LjU3MDc2MzQyMjkwOTU1XSwgWzEyNy4wODA2ODU0MTI4MDQwMywgMzcuNTY5MDY0MjU1MTkwMTddLCBbMTI3LjA3MzgyNzA3MDk5MjI3LCAzNy42MDQwMTkyODk4NjQxOV0sIFsxMjcuMDczNTEyNDM4MjUyNzgsIDM3LjYxMjgzNjYwMzQyMzEzXV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWM5MTFcdWI3OTFcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTA3MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjOTExXHViNzkxXHVhZDZjIiwgIm5hbWVfZW5nIjogIkp1bmduYW5nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M5OTRjNyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjAyNTI3MjU0NTI4MDAzLCAzNy41NzUyNDYxNjI0NTI0OV0sIFsxMjcuMDQyNzA1MjIyMDk0LCAzNy41OTIzOTQzNzU5MzM5MV0sIFsxMjcuMDczODI3MDcwOTkyMjcsIDM3LjYwNDAxOTI4OTg2NDE5XSwgWzEyNy4wODA2ODU0MTI4MDQwMywgMzcuNTY5MDY0MjU1MTkwMTddLCBbMTI3LjA3NDIxMDUzMDI0MzYyLCAzNy41NTcyNDc2OTcxMjA4NV0sIFsxMjcuMDUwMDU2MDEwODE1NjcsIDM3LjU2NzU3NzYxMjU5MDg0Nl0sIFsxMjcuMDI1NDcyNjYzNDk5NzYsIDM3LjU2ODk0MzU1MjIzNzczNF0sIFsxMjcuMDI1MjcyNTQ1MjgwMDMsIDM3LjU3NTI0NjE2MjQ1MjQ5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIzZDlcdWIzMDBcdWJiMzhcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTA2MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViM2Q5XHViMzAwXHViYjM4XHVhZDZjIiwgIm5hbWVfZW5nIjogIkRvbmdkYWVtdW4tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjYzk5NGM3IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XSwgWzEyNy4xMDMwNDE3NDI0OTIxNCwgMzcuNTcwNzYzNDIyOTA5NTVdLCBbMTI3LjExNTE5NTg0OTgxNjA2LCAzNy41NTc1MzMxODA3MDQ5MTVdLCBbMTI3LjExMTY3NjQyMDM2MDgsIDM3LjU0MDY2OTk1NTMyNDk2NV0sIFsxMjcuMTAwODc1MTk3OTE5NjIsIDM3LjUyNDg0MTIyMDE2NzA1NV0sIFsxMjcuMDY5MDY5ODEzMDM3MiwgMzcuNTIyMjc5NDIzNTA1MDI2XSwgWzEyNy4wNTg2NzM1OTI4ODM5OCwgMzcuNTI2Mjk5NzQ5MjI1NjhdLCBbMTI3LjA3NDIxMDUzMDI0MzYyLCAzNy41NTcyNDc2OTcxMjA4NV0sIFsxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFkMTFcdWM5YzRcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTA1MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhZDExXHVjOWM0XHVhZDZjIiwgIm5hbWVfZW5nIjogIkd3YW5namluLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2Q0YjlkYSIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdLCBbMTI3LjA1MDA1NjAxMDgxNTY3LCAzNy41Njc1Nzc2MTI1OTA4NDZdLCBbMTI3LjA3NDIxMDUzMDI0MzYyLCAzNy41NTcyNDc2OTcxMjA4NV0sIFsxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XSwgWzEyNy4wMjMwMjgzMTg5MDU1OSwgMzcuNTMyMzE4OTk1ODI2NjNdLCBbMTI3LjAxMDcwODk0MTc3NDgyLCAzNy41NDExODA0ODk2NDc2Ml0sIFsxMjcuMDI1NDcyNjYzNDk5NzYsIDM3LjU2ODk0MzU1MjIzNzczNF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMTMxXHViM2Q5XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNDAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzEzMVx1YjNkOVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJTZW9uZ2RvbmctZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjYzk5NGM3IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDEwNzA4OTQxNzc0ODIsIDM3LjU0MTE4MDQ4OTY0NzYyXSwgWzEyNy4wMjMwMjgzMTg5MDU1OSwgMzcuNTMyMzE4OTk1ODI2NjNdLCBbMTI3LjAxMzk3MTE5NjY3NTEzLCAzNy41MjUwMzk4ODI4OTY2OV0sIFsxMjYuOTgyMjM4MDc5MTYwODEsIDM3LjUwOTMxNDk2Njc3MDMyNl0sIFsxMjYuOTUyNDk5OTAyOTgxNTksIDM3LjUxNzIyNTAwNzQxODEzXSwgWzEyNi45NDU2NjczMzA4MzIxMiwgMzcuNTI2NjE3NTQyNDUzMzY2XSwgWzEyNi45NjQ0ODU3MDU1MzA1NSwgMzcuNTQ4NzA1NjkyMDIxNjM1XSwgWzEyNi45ODc1Mjk5NjkwMzMyOCwgMzcuNTUwOTQ4MTg4MDcxMzldLCBbMTI3LjAxMDcwODk0MTc3NDgyLCAzNy41NDExODA0ODk2NDc2Ml1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjNmE5XHVjMGIwXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwMzAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzZhOVx1YzBiMFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJZb25nc2FuLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M5OTRjNyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdLCBbMTI3LjAxMDcwODk0MTc3NDgyLCAzNy41NDExODA0ODk2NDc2Ml0sIFsxMjYuOTg3NTI5OTY5MDMzMjgsIDM3LjU1MDk0ODE4ODA3MTM5XSwgWzEyNi45NjQ0ODU3MDU1MzA1NSwgMzcuNTQ4NzA1NjkyMDIxNjM1XSwgWzEyNi45NjM1ODIyNjcxMDgxMiwgMzcuNTU2MDU2MzU0NzUxNTRdLCBbMTI2Ljk2ODczNjMzMjc5MDc1LCAzNy41NjMxMzYwNDY5MDgyN10sIFsxMjcuMDI1NDcyNjYzNDk5NzYsIDM3LjU2ODk0MzU1MjIzNzczNF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjOTExXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwMjAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzkxMVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJKdW5nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2NlMTI1NiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk3Mzg4NjQxMjg3MDIsIDM3LjYyOTQ5NjM0Nzg2ODg4XSwgWzEyNi45NzcxNzU0MDY0MTYsIDM3LjYyODU5NzE1NDAwMzg4XSwgWzEyNi45ODg3OTg2NTk5MjM4NCwgMzcuNjExODkyNzMxOTc1Nl0sIFsxMjYuOTkzNDgyOTMzNTgzMTQsIDM3LjU4ODU2NTQ1NzIxNjE1Nl0sIFsxMjcuMDI1MjcyNTQ1MjgwMDMsIDM3LjU3NTI0NjE2MjQ1MjQ5XSwgWzEyNy4wMjU0NzI2NjM0OTk3NiwgMzcuNTY4OTQzNTUyMjM3NzM0XSwgWzEyNi45Njg3MzYzMzI3OTA3NSwgMzcuNTYzMTM2MDQ2OTA4MjddLCBbMTI2Ljk1NTY1NDI1ODQ2NDYzLCAzNy41NzYwODA3OTA4ODE0NTZdLCBbMTI2Ljk1MjQ3NTIwMzA1NzIsIDM3LjYwNTA4NjkyNzM3MDQ1XSwgWzEyNi45NTQyNzAxNzAwNjEyOSwgMzcuNjIyMDMzNDMxMzM5NDI1XSwgWzEyNi45NzM4ODY0MTI4NzAyLCAzNy42Mjk0OTYzNDc4Njg4OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjODg1XHViODVjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwMTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1Yzg4NVx1Yjg1Y1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJKb25nbm8tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjOTEwMDNmIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifV0sICJ0eXBlIjogIkZlYXR1cmVDb2xsZWN0aW9uIn0KICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9iOTZmYzdlNTJlZGM0ZTA1YjAzYWNhMDIwMTJkODE4MCk7CiAgICAgICAgICAgICAgICBnZW9fanNvbl9kNDU4ZWIzN2Y1Yzc0NjJlOTUwMDRkMjhhZTk5ZTllYS5zZXRTdHlsZShmdW5jdGlvbihmZWF0dXJlKSB7cmV0dXJuIGZlYXR1cmUucHJvcGVydGllcy5zdHlsZTt9KTsKCiAgICAgICAgICAgIAogICAgCiAgICB2YXIgY29sb3JfbWFwXzUzNzRmODc1YWI1ODQxNzFhMDMwYzlkODU1MTkwMDk5ID0ge307CgogICAgCiAgICBjb2xvcl9tYXBfNTM3NGY4NzVhYjU4NDE3MWEwMzBjOWQ4NTUxOTAwOTkuY29sb3IgPSBkMy5zY2FsZS50aHJlc2hvbGQoKQogICAgICAgICAgICAgIC5kb21haW4oWzEuNjI5NTUxNjg0NDE3NjcxOCwgMS42ODc4MjU3OTc5NDM0MzI4LCAxLjc0NjA5OTkxMTQ2OTE5MzcsIDEuODA0Mzc0MDI0OTk0OTU0NywgMS44NjI2NDgxMzg1MjA3MTU2LCAxLjkyMDkyMjI1MjA0NjQ3NjYsIDEuOTc5MTk2MzY1NTcyMjM3NSwgMi4wMzc0NzA0NzkwOTc5OTg1LCAyLjA5NTc0NDU5MjYyMzc1OTcsIDIuMTU0MDE4NzA2MTQ5NTIwNCwgMi4yMTIyOTI4MTk2NzUyODE2LCAyLjI3MDU2NjkzMzIwMTA0MjMsIDIuMzI4ODQxMDQ2NzI2ODAzNSwgMi4zODcxMTUxNjAyNTI1NjQyLCAyLjQ0NTM4OTI3Mzc3ODMyNTQsIDIuNTAzNjYzMzg3MzA0MDg2MSwgMi41NjE5Mzc1MDA4Mjk4NDczLCAyLjYyMDIxMTYxNDM1NTYwODUsIDIuNjc4NDg1NzI3ODgxMzY5MiwgMi43MzY3NTk4NDE0MDcxMjk5LCAyLjc5NTAzMzk1NDkzMjg5MTEsIDIuODUzMzA4MDY4NDU4NjUyMywgMi45MTE1ODIxODE5ODQ0MTM0LCAyLjk2OTg1NjI5NTUxMDE3NDIsIDMuMDI4MTMwNDA5MDM1OTM0OSwgMy4wODY0MDQ1MjI1NjE2OTYxLCAzLjE0NDY3ODYzNjA4NzQ1NjgsIDMuMjAyOTUyNzQ5NjEzMjE3NSwgMy4yNjEyMjY4NjMxMzg5Nzg3LCAzLjMxOTUwMDk3NjY2NDczOTksIDMuMzc3Nzc1MDkwMTkwNTAxLCAzLjQzNjA0OTIwMzcxNjI2MTgsIDMuNDk0MzIzMzE3MjQyMDIyNSwgMy41NTI1OTc0MzA3Njc3ODM3LCAzLjYxMDg3MTU0NDI5MzU0NDgsIDMuNjY5MTQ1NjU3ODE5MzA1MSwgMy43Mjc0MTk3NzEzNDUwNjYzLCAzLjc4NTY5Mzg4NDg3MDgyNzUsIDMuODQzOTY3OTk4Mzk2NTg4NiwgMy45MDIyNDIxMTE5MjIzNDg5LCAzLjk2MDUxNjIyNTQ0ODExMDEsIDQuMDE4NzkwMzM4OTczODcxMywgNC4wNzcwNjQ0NTI0OTk2MzI1LCA0LjEzNTMzODU2NjAyNTM5MzYsIDQuMTkzNjEyNjc5NTUxMTU0OCwgNC4yNTE4ODY3OTMwNzY5MTUxLCA0LjMxMDE2MDkwNjYwMjY3NjMsIDQuMzY4NDM1MDIwMTI4NDM3NCwgNC40MjY3MDkxMzM2NTQxOTc3LCA0LjQ4NDk4MzI0NzE3OTk1ODksIDQuNTQzMjU3MzYwNzA1NzIwMSwgNC42MDE1MzE0NzQyMzE0ODEyLCA0LjY1OTgwNTU4Nzc1NzI0MTUsIDQuNzE4MDc5NzAxMjgzMDAyNywgNC43NzYzNTM4MTQ4MDg3NjM5LCA0LjgzNDYyNzkyODMzNDUyNSwgNC44OTI5MDIwNDE4NjAyODYyLCA0Ljk1MTE3NjE1NTM4NjA0NzQsIDUuMDA5NDUwMjY4OTExODA3NywgNS4wNjc3MjQzODI0Mzc1Njg4LCA1LjEyNTk5ODQ5NTk2MzMzLCA1LjE4NDI3MjYwOTQ4OTA5MTIsIDUuMjQyNTQ2NzIzMDE0ODUxNSwgNS4zMDA4MjA4MzY1NDA2MTI2LCA1LjM1OTA5NDk1MDA2NjM3MzgsIDUuNDE3MzY5MDYzNTkyMTM0MSwgNS40NzU2NDMxNzcxMTc4OTUzLCA1LjUzMzkxNzI5MDY0MzY1NjUsIDUuNTkyMTkxNDA0MTY5NDE3NiwgNS42NTA0NjU1MTc2OTUxNzg4LCA1LjcwODczOTYzMTIyMDkzOTEsIDUuNzY3MDEzNzQ0NzQ2NzAwMywgNS44MjUyODc4NTgyNzI0NjE0LCA1Ljg4MzU2MTk3MTc5ODIyMjYsIDUuOTQxODM2MDg1MzIzOTgyOSwgNi4wMDAxMTAxOTg4NDk3NDQxLCA2LjA1ODM4NDMxMjM3NTUwNTIsIDYuMTE2NjU4NDI1OTAxMjY2NCwgNi4xNzQ5MzI1Mzk0MjcwMjY3LCA2LjIzMzIwNjY1Mjk1Mjc4NzksIDYuMjkxNDgwNzY2NDc4NTQ5LCA2LjM0OTc1NDg4MDAwNDMxMDIsIDYuNDA4MDI4OTkzNTMwMDcxNCwgNi40NjYzMDMxMDcwNTU4MzI2LCA2LjUyNDU3NzIyMDU4MTU5MzcsIDYuNTgyODUxMzM0MTA3MzU0LCA2LjY0MTEyNTQ0NzYzMzExNTIsIDYuNjk5Mzk5NTYxMTU4ODc2NCwgNi43NTc2NzM2NzQ2ODQ2Mzc1LCA2LjgxNTk0Nzc4ODIxMDM5NzgsIDYuODc0MjIxOTAxNzM2MTU5LCA2LjkzMjQ5NjAxNTI2MTkyMDIsIDYuOTkwNzcwMTI4Nzg3NjgxMywgNy4wNDkwNDQyNDIzMTM0NDE2LCA3LjEwNzMxODM1NTgzOTIwMjgsIDcuMTY1NTkyNDY5MzY0OTY0LCA3LjIyMzg2NjU4Mjg5MDcyNDMsIDcuMjgyMTQwNjk2NDE2NDg1NCwgNy4zNDA0MTQ4MDk5NDIyNDY2LCA3LjM5ODY4ODkyMzQ2ODAwNzgsIDcuNDU2OTYzMDM2OTkzNzY4MSwgNy41MTUyMzcxNTA1MTk1MjkyLCA3LjU3MzUxMTI2NDA0NTI5MDQsIDcuNjMxNzg1Mzc3NTcxMDUxNiwgNy42OTAwNTk0OTEwOTY4MTE5LCA3Ljc0ODMzMzYwNDYyMjU3MywgNy44MDY2MDc3MTgxNDgzMzQyLCA3Ljg2NDg4MTgzMTY3NDA5NTQsIDcuOTIzMTU1OTQ1MTk5ODU1NywgNy45ODE0MzAwNTg3MjU2MTY4LCA4LjAzOTcwNDE3MjI1MTM3OCwgOC4wOTc5NzgyODU3NzcxMzgzLCA4LjE1NjI1MjM5OTMwMjkwMDQsIDguMjE0NTI2NTEyODI4NjYwNiwgOC4yNzI4MDA2MjYzNTQ0MjI3LCA4LjMzMTA3NDczOTg4MDE4MywgOC4zODkzNDg4NTM0MDU5NDMzLCA4LjQ0NzYyMjk2NjkzMTcwNTMsIDguNTA1ODk3MDgwNDU3NDY1NiwgOC41NjQxNzExOTM5ODMyMjU5LCA4LjYyMjQ0NTMwNzUwODk4OCwgOC42ODA3MTk0MjEwMzQ3NDgzLCA4LjczODk5MzUzNDU2MDUxMDMsIDguNzk3MjY3NjQ4MDg2MjcwNiwgOC44NTU1NDE3NjE2MTIwMzA5LCA4LjkxMzgxNTg3NTEzNzc5MjksIDguOTcyMDg5OTg4NjYzNTUzMiwgOS4wMzAzNjQxMDIxODkzMTM1LCA5LjA4ODYzODIxNTcxNTA3NTYsIDkuMTQ2OTEyMzI5MjQwODM1OSwgOS4yMDUxODY0NDI3NjY1OTYxLCA5LjI2MzQ2MDU1NjI5MjM1ODIsIDkuMzIxNzM0NjY5ODE4MTE4NSwgOS4zODAwMDg3ODMzNDM4ODA2LCA5LjQzODI4Mjg5Njg2OTY0MDgsIDkuNDk2NTU3MDEwMzk1NDAxMSwgOS41NTQ4MzExMjM5MjExNjMyLCA5LjYxMzEwNTIzNzQ0NjkyMzUsIDkuNjcxMzc5MzUwOTcyNjg1NSwgOS43Mjk2NTM0NjQ0OTg0NDU4LCA5Ljc4NzkyNzU3ODAyNDIwNjEsIDkuODQ2MjAxNjkxNTQ5OTY4MiwgOS45MDQ0NzU4MDUwNzU3Mjg0LCA5Ljk2Mjc0OTkxODYwMTQ5MDUsIDEwLjAyMTAyNDAzMjEyNzI1MSwgMTAuMDc5Mjk4MTQ1NjUzMDEzLCAxMC4xMzc1NzIyNTkxNzg3NzMsIDEwLjE5NTg0NjM3MjcwNDUzMywgMTAuMjU0MTIwNDg2MjMwMjk0LCAxMC4zMTIzOTQ1OTk3NTYwNTYsIDEwLjM3MDY2ODcxMzI4MTgxNiwgMTAuNDI4OTQyODI2ODA3NTc4LCAxMC40ODcyMTY5NDAzMzMzMzgsIDEwLjU0NTQ5MTA1Mzg1OTEsIDEwLjYwMzc2NTE2NzM4NDg2MSwgMTAuNjYyMDM5MjgwOTEwNjIxLCAxMC43MjAzMTMzOTQ0MzYzODEsIDEwLjc3ODU4NzUwNzk2MjE0MywgMTAuODM2ODYxNjIxNDg3OTA0LCAxMC44OTUxMzU3MzUwMTM2NjYsIDEwLjk1MzQwOTg0ODUzOTQyNiwgMTEuMDExNjgzOTYyMDY1MTg4LCAxMS4wNjk5NTgwNzU1OTA5NDgsIDExLjEyODIzMjE4OTExNjcwOSwgMTEuMTg2NTA2MzAyNjQyNDcxLCAxMS4yNDQ3ODA0MTYxNjgyMzEsIDExLjMwMzA1NDUyOTY5Mzk5MywgMTEuMzYxMzI4NjQzMjE5NzUzLCAxMS40MTk2MDI3NTY3NDU1MTUsIDExLjQ3Nzg3Njg3MDI3MTI3NiwgMTEuNTM2MTUwOTgzNzk3MDM2LCAxMS41OTQ0MjUwOTczMjI3OTYsIDExLjY1MjY5OTIxMDg0ODU1OCwgMTEuNzEwOTczMzI0Mzc0MzE5LCAxMS43NjkyNDc0Mzc5MDAwODEsIDExLjgyNzUyMTU1MTQyNTg0MSwgMTEuODg1Nzk1NjY0OTUxNjAzLCAxMS45NDQwNjk3Nzg0NzczNjIsIDEyLjAwMjM0Mzg5MjAwMzEyNCwgMTIuMDYwNjE4MDA1NTI4ODg0LCAxMi4xMTg4OTIxMTkwNTQ2NDYsIDEyLjE3NzE2NjIzMjU4MDQwNiwgMTIuMjM1NDQwMzQ2MTA2MTY4LCAxMi4yOTM3MTQ0NTk2MzE5MjksIDEyLjM1MTk4ODU3MzE1NzY5MSwgMTIuNDEwMjYyNjg2NjgzNDQ5LCAxMi40Njg1MzY4MDAyMDkyMTEsIDEyLjUyNjgxMDkxMzczNDk3MSwgMTIuNTg1MDg1MDI3MjYwNzM0LCAxMi42NDMzNTkxNDA3ODY0OTQsIDEyLjcwMTYzMzI1NDMxMjI1NiwgMTIuNzU5OTA3MzY3ODM4MDE2LCAxMi44MTgxODE0ODEzNjM3NzYsIDEyLjg3NjQ1NTU5NDg4OTUzOSwgMTIuOTM0NzI5NzA4NDE1Mjk5LCAxMi45OTMwMDM4MjE5NDEwNjEsIDEzLjA1MTI3NzkzNTQ2NjgyMSwgMTMuMTA5NTUyMDQ4OTkyNTgzLCAxMy4xNjc4MjYxNjI1MTgzNDMsIDEzLjIyNjEwMDI3NjA0NDEwNiwgMTMuMjg0Mzc0Mzg5NTY5ODY0LCAxMy4zNDI2NDg1MDMwOTU2MjYsIDEzLjQwMDkyMjYxNjYyMTM4NiwgMTMuNDU5MTk2NzMwMTQ3MTQ4LCAxMy41MTc0NzA4NDM2NzI5MDksIDEzLjU3NTc0NDk1NzE5ODY3MSwgMTMuNjM0MDE5MDcwNzI0NDMxLCAxMy42OTIyOTMxODQyNTAxOTMsIDEzLjc1MDU2NzI5Nzc3NTk1MiwgMTMuODA4ODQxNDExMzAxNzE0LCAxMy44NjcxMTU1MjQ4Mjc0NzQsIDEzLjkyNTM4OTYzODM1MzIzNiwgMTMuOTgzNjYzNzUxODc4OTk2LCAxNC4wNDE5Mzc4NjU0MDQ3NTgsIDE0LjEwMDIxMTk3ODkzMDUxOSwgMTQuMTU4NDg2MDkyNDU2Mjc5LCAxNC4yMTY3NjAyMDU5ODIwMzksIDE0LjI3NTAzNDMxOTUwNzgwMSwgMTQuMzMzMzA4NDMzMDMzNTYyLCAxNC4zOTE1ODI1NDY1NTkzMjQsIDE0LjQ0OTg1NjY2MDA4NTA4NCwgMTQuNTA4MTMwNzczNjEwODQ2LCAxNC41NjY0MDQ4ODcxMzY2MDUsIDE0LjYyNDY3OTAwMDY2MjM2NywgMTQuNjgyOTUzMTE0MTg4MTI5LCAxNC43NDEyMjcyMjc3MTM4ODksIDE0Ljc5OTUwMTM0MTIzOTY1MSwgMTQuODU3Nzc1NDU0NzY1NDExLCAxNC45MTYwNDk1NjgyOTExNzMsIDE0Ljk3NDMyMzY4MTgxNjkzNCwgMTUuMDMyNTk3Nzk1MzQyNjk0LCAxNS4wOTA4NzE5MDg4Njg0NTQsIDE1LjE0OTE0NjAyMjM5NDIxNiwgMTUuMjA3NDIwMTM1OTE5OTc3LCAxNS4yNjU2OTQyNDk0NDU3MzksIDE1LjMyMzk2ODM2Mjk3MTQ5OSwgMTUuMzgyMjQyNDc2NDk3MjYxLCAxNS40NDA1MTY1OTAwMjMwMjEsIDE1LjQ5ODc5MDcwMzU0ODc4MiwgMTUuNTU3MDY0ODE3MDc0NTQyLCAxNS42MTUzMzg5MzA2MDAzMDQsIDE1LjY3MzYxMzA0NDEyNjA2NCwgMTUuNzMxODg3MTU3NjUxODI2LCAxNS43OTAxNjEyNzExNzc1ODYsIDE1Ljg0ODQzNTM4NDcwMzM0OSwgMTUuOTA2NzA5NDk4MjI5MTA3LCAxNS45NjQ5ODM2MTE3NTQ4NjksIDE2LjAyMzI1NzcyNTI4MDYyOSwgMTYuMDgxNTMxODM4ODA2MzkxLCAxNi4xMzk4MDU5NTIzMzIxNSwgMTYuMTk4MDgwMDY1ODU3OTEyLCAxNi4yNTYzNTQxNzkzODM2NzQsIDE2LjMxNDYyODI5MjkwOTQzNiwgMTYuMzcyOTAyNDA2NDM1MTk1LCAxNi40MzExNzY1MTk5NjA5NTcsIDE2LjQ4OTQ1MDYzMzQ4NjcxNSwgMTYuNTQ3NzI0NzQ3MDEyNDc3LCAxNi42MDU5OTg4NjA1MzgyMzksIDE2LjY2NDI3Mjk3NDA2NDAwMSwgMTYuNzIyNTQ3MDg3NTg5NzYzLCAxNi43ODA4MjEyMDExMTU1MjIsIDE2LjgzOTA5NTMxNDY0MTI4NCwgMTYuODk3MzY5NDI4MTY3MDQzLCAxNi45NTU2NDM1NDE2OTI4MDUsIDE3LjAxMzkxNzY1NTIxODU2NywgMTcuMDcyMTkxNzY4NzQ0MzI5LCAxNy4xMzA0NjU4ODIyNzAwODcsIDE3LjE4ODczOTk5NTc5NTg0OSwgMTcuMjQ3MDE0MTA5MzIxNjA4LCAxNy4zMDUyODgyMjI4NDczNywgMTcuMzYzNTYyMzM2MzczMTMyLCAxNy40MjE4MzY0NDk4OTg4OTQsIDE3LjQ4MDExMDU2MzQyNDY1MywgMTcuNTM4Mzg0Njc2OTUwNDE1LCAxNy41OTY2NTg3OTA0NzYxNzcsIDE3LjY1NDkzMjkwNDAwMTkzNSwgMTcuNzEzMjA3MDE3NTI3Njk3LCAxNy43NzE0ODExMzEwNTM0NTksIDE3LjgyOTc1NTI0NDU3OTIxOCwgMTcuODg4MDI5MzU4MTA0OTgsIDE3Ljk0NjMwMzQ3MTYzMDczOCwgMTguMDA0NTc3NTg1MTU2NSwgMTguMDYyODUxNjk4NjgyMjYyLCAxOC4xMjExMjU4MTIyMDgwMjUsIDE4LjE3OTM5OTkyNTczMzc4MywgMTguMjM3Njc0MDM5MjU5NTQ1LCAxOC4yOTU5NDgxNTI3ODUzMDcsIDE4LjM1NDIyMjI2NjMxMTA2NiwgMTguNDEyNDk2Mzc5ODM2ODI4LCAxOC40NzA3NzA0OTMzNjI1OSwgMTguNTI5MDQ0NjA2ODg4MzUyLCAxOC41ODczMTg3MjA0MTQxMSwgMTguNjQ1NTkyODMzOTM5ODcyLCAxOC43MDM4NjY5NDc0NjU2MzQsIDE4Ljc2MjE0MTA2MDk5MTM5MywgMTguODIwNDE1MTc0NTE3MTU1LCAxOC44Nzg2ODkyODgwNDI5MTQsIDE4LjkzNjk2MzQwMTU2ODY3OSwgMTguOTk1MjM3NTE1MDk0NDM4LCAxOS4wNTM1MTE2Mjg2MjAyLCAxOS4xMTE3ODU3NDIxNDU5NTgsIDE5LjE3MDA1OTg1NTY3MTcyNCwgMTkuMjI4MzMzOTY5MTk3NDgyLCAxOS4yODY2MDgwODI3MjMyNDEsIDE5LjM0NDg4MjE5NjI0OTAwMywgMTkuNDAzMTU2MzA5Nzc0NzY1LCAxOS40NjE0MzA0MjMzMDA1MjcsIDE5LjUxOTcwNDUzNjgyNjI4NiwgMTkuNTc3OTc4NjUwMzUyMDQ4LCAxOS42MzYyNTI3NjM4Nzc4MSwgMTkuNjk0NTI2ODc3NDAzNTY4LCAxOS43NTI4MDA5OTA5MjkzMywgMTkuODExMDc1MTA0NDU1MDg5LCAxOS44NjkzNDkyMTc5ODA4NTQsIDE5LjkyNzYyMzMzMTUwNjYxMywgMTkuOTg1ODk3NDQ1MDMyMzc1LCAyMC4wNDQxNzE1NTg1NTgxMzMsIDIwLjEwMjQ0NTY3MjA4Mzg5NiwgMjAuMTYwNzE5Nzg1NjA5NjU4LCAyMC4yMTg5OTM4OTkxMzU0MTYsIDIwLjI3NzI2ODAxMjY2MTE3OCwgMjAuMzM1NTQyMTI2MTg2OTQsIDIwLjM5MzgxNjIzOTcxMjcwMiwgMjAuNDUyMDkwMzUzMjM4NDYxLCAyMC41MTAzNjQ0NjY3NjQyMjMsIDIwLjU2ODYzODU4MDI4OTk4NSwgMjAuNjI2OTEyNjkzODE1NzQzLCAyMC42ODUxODY4MDczNDE1MDUsIDIwLjc0MzQ2MDkyMDg2NzI2OCwgMjAuODAxNzM1MDM0MzkzMDMsIDIwLjg2MDAwOTE0NzkxODc4OCwgMjAuOTE4MjgzMjYxNDQ0NTUsIDIwLjk3NjU1NzM3NDk3MDMxMiwgMjEuMDM0ODMxNDg4NDk2MDcxLCAyMS4wOTMxMDU2MDIwMjE4MzMsIDIxLjE1MTM3OTcxNTU0NzU5MSwgMjEuMjA5NjUzODI5MDczMzU3LCAyMS4yNjc5Mjc5NDI1OTkxMTUsIDIxLjMyNjIwMjA1NjEyNDg3OCwgMjEuMzg0NDc2MTY5NjUwNjM2LCAyMS40NDI3NTAyODMxNzYzOTgsIDIxLjUwMTAyNDM5NjcwMjE2LCAyMS41NTkyOTg1MTAyMjc5MTksIDIxLjYxNzU3MjYyMzc1MzY4MSwgMjEuNjc1ODQ2NzM3Mjc5NDQzLCAyMS43MzQxMjA4NTA4MDUyMDUsIDIxLjc5MjM5NDk2NDMzMDk2MywgMjEuODUwNjY5MDc3ODU2NzIyLCAyMS45MDg5NDMxOTEzODI0ODcsIDIxLjk2NzIxNzMwNDkwODI0NiwgMjIuMDI1NDkxNDE4NDM0MDA4LCAyMi4wODM3NjU1MzE5NTk3NjcsIDIyLjE0MjAzOTY0NTQ4NTUzMiwgMjIuMjAwMzEzNzU5MDExMjkxLCAyMi4yNTg1ODc4NzI1MzcwNDksIDIyLjMxNjg2MTk4NjA2MjgxNSwgMjIuMzc1MTM2MDk5NTg4NTczLCAyMi40MzM0MTAyMTMxMTQzMzUsIDIyLjQ5MTY4NDMyNjY0MDA5NCwgMjIuNTQ5OTU4NDQwMTY1ODU5LCAyMi42MDgyMzI1NTM2OTE2MTgsIDIyLjY2NjUwNjY2NzIxNzM4LCAyMi43MjQ3ODA3ODA3NDMxMzksIDIyLjc4MzA1NDg5NDI2ODkwMSwgMjIuODQxMzI5MDA3Nzk0NjYzLCAyMi44OTk2MDMxMjEzMjA0MjEsIDIyLjk1Nzg3NzIzNDg0NjE4MywgMjMuMDE2MTUxMzQ4MzcxOTQ1LCAyMy4wNzQ0MjU0NjE4OTc3MDcsIDIzLjEzMjY5OTU3NTQyMzQ2NiwgMjMuMTkwOTczNjg4OTQ5MjI0LCAyMy4yNDkyNDc4MDI0NzQ5OSwgMjMuMzA3NTIxOTE2MDAwNzQ5LCAyMy4zNjU3OTYwMjk1MjY1MTEsIDIzLjQyNDA3MDE0MzA1MjI2OSwgMjMuNDgyMzQ0MjU2NTc4MDM1LCAyMy41NDA2MTgzNzAxMDM3OTMsIDIzLjU5ODg5MjQ4MzYyOTU1MiwgMjMuNjU3MTY2NTk3MTU1MzE0LCAyMy43MTU0NDA3MTA2ODEwNzYsIDIzLjc3MzcxNDgyNDIwNjgzOCwgMjMuODMxOTg4OTM3NzMyNTk2LCAyMy44OTAyNjMwNTEyNTgzNTgsIDIzLjk0ODUzNzE2NDc4NDEyMSwgMjQuMDA2ODExMjc4MzA5ODc5LCAyNC4wNjUwODUzOTE4MzU2NDEsIDI0LjEyMzM1OTUwNTM2MTQwMywgMjQuMTgxNjMzNjE4ODg3MTY1LCAyNC4yMzk5MDc3MzI0MTI5MjQsIDI0LjI5ODE4MTg0NTkzODY4NiwgMjQuMzU2NDU1OTU5NDY0NDQ4LCAyNC40MTQ3MzAwNzI5OTAyMSwgMjQuNDczMDA0MTg2NTE1OTY4LCAyNC41MzEyNzgzMDAwNDE3MjcsIDI0LjU4OTU1MjQxMzU2NzQ5MywgMjQuNjQ3ODI2NTI3MDkzMjUxLCAyNC43MDYxMDA2NDA2MTkwMTMsIDI0Ljc2NDM3NDc1NDE0NDc3MiwgMjQuODIyNjQ4ODY3NjcwNTM3LCAyNC44ODA5MjI5ODExOTYyOTYsIDI0LjkzOTE5NzA5NDcyMjA1NCwgMjQuOTk3NDcxMjA4MjQ3ODE2LCAyNS4wNTU3NDUzMjE3NzM1NzgsIDI1LjExNDAxOTQzNTI5OTM0LCAyNS4xNzIyOTM1NDg4MjUwOTksIDI1LjIzMDU2NzY2MjM1MDg2MSwgMjUuMjg4ODQxNzc1ODc2NjIzLCAyNS4zNDcxMTU4ODk0MDIzODIsIDI1LjQwNTM5MDAwMjkyODE0NCwgMjUuNDYzNjY0MTE2NDUzOTAyLCAyNS41MjE5MzgyMjk5Nzk2NjgsIDI1LjU4MDIxMjM0MzUwNTQyNiwgMjUuNjM4NDg2NDU3MDMxMTg4LCAyNS42OTY3NjA1NzA1NTY5NDcsIDI1Ljc1NTAzNDY4NDA4MjcxMiwgMjUuODEzMzA4Nzk3NjA4NDcxLCAyNS44NzE1ODI5MTExMzQyMjksIDI1LjkyOTg1NzAyNDY1OTk5NSwgMjUuOTg4MTMxMTM4MTg1NzU0LCAyNi4wNDY0MDUyNTE3MTE1MTYsIDI2LjEwNDY3OTM2NTIzNzI3NCwgMjYuMTYyOTUzNDc4NzYzMDQsIDI2LjIyMTIyNzU5MjI4ODc5OCwgMjYuMjc5NTAxNzA1ODE0NTU3LCAyNi4zMzc3NzU4MTkzNDAzMTksIDI2LjM5NjA0OTkzMjg2NjA4MSwgMjYuNDU0MzI0MDQ2MzkxODQzLCAyNi41MTI1OTgxNTk5MTc2MDEsIDI2LjU3MDg3MjI3MzQ0MzM2NCwgMjYuNjI5MTQ2Mzg2OTY5MTI2LCAyNi42ODc0MjA1MDA0OTQ4ODQsIDI2Ljc0NTY5NDYxNDAyMDY0NiwgMjYuODAzOTY4NzI3NTQ2NDA1LCAyNi44NjIyNDI4NDEwNzIxNywgMjYuOTIwNTE2OTU0NTk3OTI5LCAyNi45Nzg3OTEwNjgxMjM2OTEsIDI3LjAzNzA2NTE4MTY0OTQ0OSwgMjcuMDk1MzM5Mjk1MTc1MjExLCAyNy4xNTM2MTM0MDg3MDA5NzQsIDI3LjIxMTg4NzUyMjIyNjczMiwgMjcuMjcwMTYxNjM1NzUyNDk0LCAyNy4zMjg0MzU3NDkyNzgyNTYsIDI3LjM4NjcwOTg2MjgwNDAxOCwgMjcuNDQ0OTgzOTc2MzI5Nzc3LCAyNy41MDMyNTgwODk4NTU1MzUsIDI3LjU2MTUzMjIwMzM4MTMwMSwgMjcuNjE5ODA2MzE2OTA3MDU5LCAyNy42NzgwODA0MzA0MzI4MjEsIDI3LjczNjM1NDU0Mzk1ODU4MywgMjcuNzk0NjI4NjU3NDg0MzQ2LCAyNy44NTI5MDI3NzEwMTAxMDQsIDI3LjkxMTE3Njg4NDUzNTg2NiwgMjcuOTY5NDUwOTk4MDYxNjI4LCAyOC4wMjc3MjUxMTE1ODczODcsIDI4LjA4NTk5OTIyNTExMzE0OSwgMjguMTQ0MjczMzM4NjM4OTA3LCAyOC4yMDI1NDc0NTIxNjQ2NzMsIDI4LjI2MDgyMTU2NTY5MDQzMSwgMjguMzE5MDk1Njc5MjE2MTkzLCAyOC4zNzczNjk3OTI3NDE5NTIsIDI4LjQzNTY0MzkwNjI2NzcxNCwgMjguNDkzOTE4MDE5NzkzNDc2LCAyOC41NTIxOTIxMzMzMTkyMzUsIDI4LjYxMDQ2NjI0Njg0NDk5NywgMjguNjY4NzQwMzYwMzcwNzU5LCAyOC43MjcwMTQ0NzM4OTY1MjEsIDI4Ljc4NTI4ODU4NzQyMjI3OSwgMjguODQzNTYyNzAwOTQ4MDM4LCAyOC45MDE4MzY4MTQ0NzM4MDMsIDI4Ljk2MDExMDkyNzk5OTU2MiwgMjkuMDE4Mzg1MDQxNTI1MzI0LCAyOS4wNzY2NTkxNTUwNTEwODIsIDI5LjEzNDkzMzI2ODU3Njg0OCwgMjkuMTkzMjA3MzgyMTAyNjA3LCAyOS4yNTE0ODE0OTU2MjgzNjksIDI5LjMwOTc1NTYwOTE1NDEyNywgMjkuMzY4MDI5NzIyNjc5ODg5LCAyOS40MjYzMDM4MzYyMDU2NTEsIDI5LjQ4NDU3Nzk0OTczMTQxLCAyOS41NDI4NTIwNjMyNTcxNzIsIDI5LjYwMTEyNjE3Njc4MjkzNCwgMjkuNjU5NDAwMjkwMzA4Njk2LCAyOS43MTc2NzQ0MDM4MzQ0NTQsIDI5Ljc3NTk0ODUxNzM2MDIxNywgMjkuODM0MjIyNjMwODg1OTc5LCAyOS44OTI0OTY3NDQ0MTE3MzcsIDI5Ljk1MDc3MDg1NzkzNzQ5OSwgMzAuMDA5MDQ0OTcxNDYzMjYxLCAzMC4wNjczMTkwODQ5ODkwMjMsIDMwLjEyNTU5MzE5ODUxNDc4MiwgMzAuMTgzODY3MzEyMDQwNTQsIDMwLjI0MjE0MTQyNTU2NjMwNiwgMzAuMzAwNDE1NTM5MDkyMDY0LCAzMC4zNTg2ODk2NTI2MTc4MjYsIDMwLjQxNjk2Mzc2NjE0MzU4NSwgMzAuNDc1MjM3ODc5NjY5MzUxLCAzMC41MzM1MTE5OTMxOTUxMDksIDMwLjU5MTc4NjEwNjcyMDg2OCwgMzAuNjUwMDYwMjIwMjQ2NjMsIDMwLjcwODMzNDMzMzc3MjM5Ml0pCiAgICAgICAgICAgICAgLnJhbmdlKFsnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJ10pOwogICAgCgogICAgY29sb3JfbWFwXzUzNzRmODc1YWI1ODQxNzFhMDMwYzlkODU1MTkwMDk5LnggPSBkMy5zY2FsZS5saW5lYXIoKQogICAgICAgICAgICAgIC5kb21haW4oWzEuNjI5NTUxNjg0NDIsIDMwLjcwODMzNDMzMzhdKQogICAgICAgICAgICAgIC5yYW5nZShbMCwgNDAwXSk7CgogICAgY29sb3JfbWFwXzUzNzRmODc1YWI1ODQxNzFhMDMwYzlkODU1MTkwMDk5LmxlZ2VuZCA9IEwuY29udHJvbCh7cG9zaXRpb246ICd0b3ByaWdodCd9KTsKICAgIGNvbG9yX21hcF81Mzc0Zjg3NWFiNTg0MTcxYTAzMGM5ZDg1NTE5MDA5OS5sZWdlbmQub25BZGQgPSBmdW5jdGlvbiAobWFwKSB7dmFyIGRpdiA9IEwuRG9tVXRpbC5jcmVhdGUoJ2RpdicsICdsZWdlbmQnKTsgcmV0dXJuIGRpdn07CiAgICBjb2xvcl9tYXBfNTM3NGY4NzVhYjU4NDE3MWEwMzBjOWQ4NTUxOTAwOTkubGVnZW5kLmFkZFRvKG1hcF9iOTZmYzdlNTJlZGM0ZTA1YjAzYWNhMDIwMTJkODE4MCk7CgogICAgY29sb3JfbWFwXzUzNzRmODc1YWI1ODQxNzFhMDMwYzlkODU1MTkwMDk5LnhBeGlzID0gZDMuc3ZnLmF4aXMoKQogICAgICAgIC5zY2FsZShjb2xvcl9tYXBfNTM3NGY4NzVhYjU4NDE3MWEwMzBjOWQ4NTUxOTAwOTkueCkKICAgICAgICAub3JpZW50KCJ0b3AiKQogICAgICAgIC50aWNrU2l6ZSgxKQogICAgICAgIC50aWNrVmFsdWVzKFsxLjYyOTU1MTY4NDQxNzY3MTgsIDYuNDc2MDE1NDU5MzEwMTI1MywgMTEuMzIyNDc5MjM0MjAyNTc5LCAxNi4xNjg5NDMwMDkwOTUwMzEsIDIxLjAxNTQwNjc4Mzk4NzQ4MywgMjUuODYxODcwNTU4ODc5OTM2LCAzMC43MDgzMzQzMzM3NzIzOTJdKTsKCiAgICBjb2xvcl9tYXBfNTM3NGY4NzVhYjU4NDE3MWEwMzBjOWQ4NTUxOTAwOTkuc3ZnID0gZDMuc2VsZWN0KCIubGVnZW5kLmxlYWZsZXQtY29udHJvbCIpLmFwcGVuZCgic3ZnIikKICAgICAgICAuYXR0cigiaWQiLCAnbGVnZW5kJykKICAgICAgICAuYXR0cigid2lkdGgiLCA0NTApCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDQwKTsKCiAgICBjb2xvcl9tYXBfNTM3NGY4NzVhYjU4NDE3MWEwMzBjOWQ4NTUxOTAwOTkuZyA9IGNvbG9yX21hcF81Mzc0Zjg3NWFiNTg0MTcxYTAzMGM5ZDg1NTE5MDA5OS5zdmcuYXBwZW5kKCJnIikKICAgICAgICAuYXR0cigiY2xhc3MiLCAia2V5IikKICAgICAgICAuYXR0cigidHJhbnNmb3JtIiwgInRyYW5zbGF0ZSgyNSwxNikiKTsKCiAgICBjb2xvcl9tYXBfNTM3NGY4NzVhYjU4NDE3MWEwMzBjOWQ4NTUxOTAwOTkuZy5zZWxlY3RBbGwoInJlY3QiKQogICAgICAgIC5kYXRhKGNvbG9yX21hcF81Mzc0Zjg3NWFiNTg0MTcxYTAzMGM5ZDg1NTE5MDA5OS5jb2xvci5yYW5nZSgpLm1hcChmdW5jdGlvbihkLCBpKSB7CiAgICAgICAgICByZXR1cm4gewogICAgICAgICAgICB4MDogaSA/IGNvbG9yX21hcF81Mzc0Zjg3NWFiNTg0MTcxYTAzMGM5ZDg1NTE5MDA5OS54KGNvbG9yX21hcF81Mzc0Zjg3NWFiNTg0MTcxYTAzMGM5ZDg1NTE5MDA5OS5jb2xvci5kb21haW4oKVtpIC0gMV0pIDogY29sb3JfbWFwXzUzNzRmODc1YWI1ODQxNzFhMDMwYzlkODU1MTkwMDk5LngucmFuZ2UoKVswXSwKICAgICAgICAgICAgeDE6IGkgPCBjb2xvcl9tYXBfNTM3NGY4NzVhYjU4NDE3MWEwMzBjOWQ4NTUxOTAwOTkuY29sb3IuZG9tYWluKCkubGVuZ3RoID8gY29sb3JfbWFwXzUzNzRmODc1YWI1ODQxNzFhMDMwYzlkODU1MTkwMDk5LngoY29sb3JfbWFwXzUzNzRmODc1YWI1ODQxNzFhMDMwYzlkODU1MTkwMDk5LmNvbG9yLmRvbWFpbigpW2ldKSA6IGNvbG9yX21hcF81Mzc0Zjg3NWFiNTg0MTcxYTAzMGM5ZDg1NTE5MDA5OS54LnJhbmdlKClbMV0sCiAgICAgICAgICAgIHo6IGQKICAgICAgICAgIH07CiAgICAgICAgfSkpCiAgICAgIC5lbnRlcigpLmFwcGVuZCgicmVjdCIpCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDEwKQogICAgICAgIC5hdHRyKCJ4IiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC54MDsgfSkKICAgICAgICAuYXR0cigid2lkdGgiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLngxIC0gZC54MDsgfSkKICAgICAgICAuc3R5bGUoImZpbGwiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLno7IH0pOwoKICAgIGNvbG9yX21hcF81Mzc0Zjg3NWFiNTg0MTcxYTAzMGM5ZDg1NTE5MDA5OS5nLmNhbGwoY29sb3JfbWFwXzUzNzRmODc1YWI1ODQxNzFhMDMwYzlkODU1MTkwMDk5LnhBeGlzKS5hcHBlbmQoInRleHQiKQogICAgICAgIC5hdHRyKCJjbGFzcyIsICJjYXB0aW9uIikKICAgICAgICAuYXR0cigieSIsIDIxKQogICAgICAgIC50ZXh0KCcnKTsKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
population
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
      <th>세대</th>
      <th>인구수</th>
      <th>세대당인구</th>
      <th>65세이상고령자</th>
      <th>고령비율</th>
      <th>맥도널드</th>
      <th>맥버거비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>231219</td>
      <td>557865</td>
      <td>2.39</td>
      <td>65859</td>
      <td>11.805544</td>
      <td>11</td>
      <td>19.718032</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>177490</td>
      <td>438225</td>
      <td>2.45</td>
      <td>56983</td>
      <td>13.003138</td>
      <td>4</td>
      <td>9.127731</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>143139</td>
      <td>327511</td>
      <td>2.26</td>
      <td>57002</td>
      <td>17.404606</td>
      <td>5</td>
      <td>15.266663</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>256042</td>
      <td>608361</td>
      <td>2.35</td>
      <td>77381</td>
      <td>12.719586</td>
      <td>4</td>
      <td>6.575043</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>258536</td>
      <td>522292</td>
      <td>1.95</td>
      <td>70807</td>
      <td>13.556976</td>
      <td>1</td>
      <td>1.914638</td>
    </tr>
    <tr>
      <th>광진구</th>
      <td>161407</td>
      <td>371671</td>
      <td>2.21</td>
      <td>44470</td>
      <td>11.964883</td>
      <td>2</td>
      <td>5.381103</td>
    </tr>
    <tr>
      <th>구로구</th>
      <td>171751</td>
      <td>440396</td>
      <td>2.38</td>
      <td>59838</td>
      <td>13.587317</td>
      <td>5</td>
      <td>11.353418</td>
    </tr>
    <tr>
      <th>금천구</th>
      <td>106333</td>
      <td>253344</td>
      <td>2.20</td>
      <td>34640</td>
      <td>13.673109</td>
      <td>4</td>
      <td>15.788809</td>
    </tr>
    <tr>
      <th>노원구</th>
      <td>217999</td>
      <td>555803</td>
      <td>2.53</td>
      <td>75081</td>
      <td>13.508563</td>
      <td>5</td>
      <td>8.995993</td>
    </tr>
    <tr>
      <th>도봉구</th>
      <td>137479</td>
      <td>345041</td>
      <td>2.49</td>
      <td>54293</td>
      <td>15.735231</td>
      <td>2</td>
      <td>5.796413</td>
    </tr>
    <tr>
      <th>동대문구</th>
      <td>160489</td>
      <td>364962</td>
      <td>2.18</td>
      <td>56284</td>
      <td>15.421880</td>
      <td>3</td>
      <td>8.220034</td>
    </tr>
    <tr>
      <th>동작구</th>
      <td>173544</td>
      <td>406715</td>
      <td>2.27</td>
      <td>57711</td>
      <td>14.189543</td>
      <td>4</td>
      <td>9.834897</td>
    </tr>
    <tr>
      <th>마포구</th>
      <td>170219</td>
      <td>385624</td>
      <td>2.20</td>
      <td>50122</td>
      <td>12.997635</td>
      <td>5</td>
      <td>12.965998</td>
    </tr>
    <tr>
      <th>서대문구</th>
      <td>137758</td>
      <td>324871</td>
      <td>2.27</td>
      <td>49645</td>
      <td>15.281450</td>
      <td>3</td>
      <td>9.234435</td>
    </tr>
    <tr>
      <th>서초구</th>
      <td>174225</td>
      <td>445164</td>
      <td>2.53</td>
      <td>54055</td>
      <td>12.142716</td>
      <td>6</td>
      <td>13.478179</td>
    </tr>
    <tr>
      <th>성동구</th>
      <td>134543</td>
      <td>314551</td>
      <td>2.28</td>
      <td>41752</td>
      <td>13.273523</td>
      <td>3</td>
      <td>9.537404</td>
    </tr>
    <tr>
      <th>성북구</th>
      <td>187234</td>
      <td>453902</td>
      <td>2.36</td>
      <td>66896</td>
      <td>14.737983</td>
      <td>3</td>
      <td>6.609356</td>
    </tr>
    <tr>
      <th>송파구</th>
      <td>266550</td>
      <td>671994</td>
      <td>2.50</td>
      <td>77978</td>
      <td>11.603973</td>
      <td>6</td>
      <td>8.928651</td>
    </tr>
    <tr>
      <th>양천구</th>
      <td>176559</td>
      <td>473087</td>
      <td>2.66</td>
      <td>56070</td>
      <td>11.851943</td>
      <td>5</td>
      <td>10.568881</td>
    </tr>
    <tr>
      <th>영등포구</th>
      <td>168784</td>
      <td>403988</td>
      <td>2.19</td>
      <td>54704</td>
      <td>13.540996</td>
      <td>4</td>
      <td>9.901284</td>
    </tr>
    <tr>
      <th>용산구</th>
      <td>108497</td>
      <td>245411</td>
      <td>2.12</td>
      <td>37238</td>
      <td>15.173729</td>
      <td>2</td>
      <td>8.149594</td>
    </tr>
    <tr>
      <th>은평구</th>
      <td>203431</td>
      <td>490253</td>
      <td>2.39</td>
      <td>75535</td>
      <td>15.407351</td>
      <td>3</td>
      <td>6.119289</td>
    </tr>
    <tr>
      <th>종로구</th>
      <td>73879</td>
      <td>164348</td>
      <td>2.09</td>
      <td>26429</td>
      <td>16.081121</td>
      <td>5</td>
      <td>30.423248</td>
    </tr>
    <tr>
      <th>중구</th>
      <td>60903</td>
      <td>135139</td>
      <td>2.07</td>
      <td>21655</td>
      <td>16.024242</td>
      <td>3</td>
      <td>22.199365</td>
    </tr>
    <tr>
      <th>중랑구</th>
      <td>179600</td>
      <td>411552</td>
      <td>2.27</td>
      <td>59992</td>
      <td>14.577016</td>
      <td>3</td>
      <td>7.289480</td>
    </tr>
  </tbody>
</table>
</div>




```python
population.to_csv('data/seoul_population_mac-idx.csv', sep=',', encoding='euc-kr')
```

### <font color='brown'> seqborn이 제공해주는 pairplot 을 사용해서 분석 </font>


```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
sns.set_style('darkgrid')
sns.set(font="Malgun Gothic")
sns.set_color_codes()

%matplotlib inline

```


```python
sns.pairplot(population, vars=["맥버거비율", "인구수", "65세이상고령자"], kind="reg");
```


![png](output_51_0.png)



```python
sns.pairplot(population, vars=["맥버거비율", "인구수", "고령비율"], kind="reg");
```


![png](output_52_0.png)



```python
sns.pairplot(population, vars=["맥버거비율", "고령비율", "인구수", "65세이상고령자"], kind="reg");
```


![png](output_53_0.png)


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
