# Tworld

SKT Tworld 데이터 가져오기
* 필요사항

  * chrome driver가 필요합니다.<br>
[chrome-driver](https://sites.google.com/a/chromium.org/chromedriver/home)
에서 드라이버를 다운로드받아 디렉토리로 복사하세요

* 유의사항
1일 로그인횟수 제한이 있네요(30회/일)
크론으로 돌리실 분은 2880초 쉬어주면 됩니다.


* 사용법 
  
<pre><code>
from Tworld import Tworld

user_id="아이디"
user_pass="패스워드"

tworld = Tworld()
if tworld.login(user_id, user_pass):
    print(tworld.get_available_data_in_mb())
</code>
</pre>
<img src='https://user-images.githubusercontent.com/6409339/40640576-90833536-6351-11e8-9996-bcf72627fa42.png'>
