**3개 py파일중 실질적 역할을 하는건 evaluation.py 하나뿐**<br>
    gt,pred는 각각 truck의 groundtruth, prediction을 car로 바꾸는 파일일 뿐이다.


**우선 yolov3에서 validation을 거쳐 result에 valid한거 저장되있다 가정.**

  1. git clone해서 일단 다운
  2. *mAP_predict 변환 코드* 폴더 들어가기
  3. 폴더로 들어가면 makefile있을 거다. terminal에서 거기로 이동
  4. make 치면 실행파일 만들어진다.
  5. .py 코드들 보면 디렉토리가 다 다르다. 수정 ㄱㄱ
  6. *evaluation.py* 실행하면 끝.<br><br>

**즉, 설치가 끝나고, mAP 구하는 과정은 크게 정리하면**
   1) yolov3 valid 실행.
   2) evaluation.py 실행.
