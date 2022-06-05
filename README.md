# Bitcoin_predict
딥러닝 없이 영상처리만 이용한 비트코인 자동투자 프로그램

## 주제 : 영상처리를 이용한 비트코인 자동 투자 도우미 프로그램
프로젝트 개요 - API를 사용하여 가격을 불러올 경우 다양한 투자지표를 사용하기 위해 직접 구현해야 하며 시간이 많이 든다. 영상처리 프로그래밍 과목에서 수강한 내용을 바탕으로 여러가지 투자 지표를 코딩을 통해 구현하는 것이 아닌 그래프에 나타나는 정보를 영상처리를 통해 효과적으로 해결할 수 있다고 생각하였다. 따라서 그래프 모양을 보고 투자를 도와줄 수 있는 투자 도우미 프로그램을 만들어 보았다. 빗썸에서는 다양한 영상처리 기법을 사용하여 처리를 하였으며, 업비트에서는 간단한 영상처리만 사용하여 둘의 차이를 비교해 보았다.

## 사용한 기술 요약
-	대비 증가 후 역방향 사상을 통한 알파벳 검출
-	격자 제거 후 엣지 검출을 위한 블러링 및 Canny Edge 검출 사용
-	Canny Edge 검출 후 모폴로지 팽창 연산 사용
-	간단한 매수 알고리즘을 통한 자동 매수 기능

## Installation

``` 
pip install pyupbit
pip install pybithumb
pip install opencv-python
... 
```

## 사용 방법
예측하고자 하는 거래소를 킨 후 Main.py를 Anaconda Prompt에서 실행시킨다. 이 때 내가 예측하고자 하는 사이트, 발급받은 API 키, 모드를 입력한다.
 
 ``` python:
python main.py --stock_exchange "bithumb" --Access_key "Input Your Access Key" 
      --Secret_key = "Input Your Secret Key" mode = "bright"
```

--stock_exchange : 거래소를 지정해주며 upbit와 bihumb 두 개가 있으며 default는 upbit이다.  <br> 
--Access_key : 해당 거래소에서 발급받은 API키 중 Access key를 넣어준다. <br>
--Secret_key : 해당 거래소에서 발급받은 API키 중 Secret Key를 넣어준다. 위의 키를 넣어주지 않는다면 거래 창에서 거래가 진행되지 않는다. <br>
--Mode : bright Mode와 dark 모드가 있으며 업비트에서는 dark모드가 지원된다.<br> 
--monitorsize : 모니터의 크기를 넣어주면 해당 모니터의 비율에 따라 출력 이미지를 자동으로 지정한다. Default는 (1920,1080)이다. <br>
해당 그래프의 예측 결과가 상승이면 매수를 진행하며, 하락이면 그대로 프로그램을 종료한다.

<br>

![image](https://user-images.githubusercontent.com/38518648/172057628-47185eb5-b71a-4bb5-9fb1-452683e560e3.png)
![image](https://user-images.githubusercontent.com/38518648/172057634-54e35e64-f6c7-4e2a-9a5e-9bc26acf4a20.png)
![image](https://user-images.githubusercontent.com/38518648/172057637-6d3141f5-9f22-48e5-b536-57ce0c4620f3.png)
<img src = "https://user-images.githubusercontent.com/38518648/172057693-71ee33e4-a0bd-4124-9fd1-5522e7c77b30.png" width = 50%>


### Edge 검출 후 사진
<img src = "https://user-images.githubusercontent.com/38518648/172057815-dcac01c3-f570-498c-b155-92ae03e441dc.png" width = 50%>
<img src = "https://user-images.githubusercontent.com/38518648/172057966-21167702-87bd-428e-a820-02195b340af2.png" width = 50%>
