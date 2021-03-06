from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic import UpdateView
import requests
from .models import Person
from .forms import PersonForm
import random

# Create your views here.

class PersonCreateView(CreateView):
    model : Person
    fields = ('name')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'jobs/index.html'

def index(request):
    return render(request, 'jobs/index.html', {'form':PersonForm()})

def past_life(request):
    my_name = request.POST.get('name')
    
    person = Person.objects.filter(name=my_name)
    # DB에 기존 회원이 있다면?
    if person:
        person = Person.objects.get(name=my_name)
    # DB에 기존 회원이 없다면?
    else:
        job_past = ['관리자', '군인', '관리자', '국회의원', '지방의회의원', '중앙정부 고위공무원', '대표이사', '게임 프로그래머', '비디오 게임 기획자', '건축가', '항공기 조종사', '항공기관사', '선장', '항해사', '도선사', '관제사', '전문 의사', '일반 의사', '한의사', '치과 의사', '수의사', '약사', '한약사', '간호사', '보건 교사', '영양사', '영양 교사', '임상병리사', '방사선사', '치과기공사', '치과위생사', '물리치료사', '작업치료사', '정신보건 임상심리사', '언어치료사', '안경사', '보건의료정보관리사', '간호조무사', '사회복지사', '청소년 지도사', '목사', '신부', '승려', '교무', '수녀 및 수사', '전도사', '대학 교수', '대학 시간강사', '학교 교사', '국어 교사', '수학 교사', '사회 교사', '과학 교사', '음악교사', '미술교사', '체육교사', '가정 교사', '영어교사', '초등학교 교사', '특수교육 교사', '장학사', '대학 교육조교', '판사', '검사', '변호사', '법무사', '집행관', '변리사', '노무사', '회계사', '세무사', '관세사', '투자 및 금융 분석가', '신용 분석가', '보험계리사', '손해사정인', '감정평가사', '감정사', '소믈리에', '조향사', '부동산 중개인', '방송작가', '작가', '평론가', '시인', '소설가', '영화 평론가', '각본가', '번역가', '통역가', '기자', '큐레이터', '사서', '감독', '배우', '개그맨', '코미디언', '모델', '패션 모델', '성우', '스턴트맨', '보조출연자', '아나운서', '리포터', '쇼핑호스트', '비디오자키', '디스크자키', '화가', '조각가', '사진가', '만화가', '만화영화 작가', '국악인', '지휘자', '작곡가', '가수', '성악가', '안무가', '디자이너', '제품 디자이너', '자동차 디자이너', '패션 디자이너', '인테리어 디자이너', '무대 및 세트 디자이너', '시각 디자이너', '북 디자이너', '삽화가', '활자 디자이너', '웹 디자이너', '게임그래픽 디자이너', '경기감독 및 코치', '직업 운동선수', '경기심판', '트레이너', '수영강사', '바둑기사', '프로게이머', '연예인 및 스포츠 매니저', '마술사', '곡예사', '조련사', '비서', '법무 사무원', '속기사', '경찰관', '소방관', '교도관', '경호원', '간병인', '미용사', '장의사', '점술가', '무당', '항공기 객실승무원', '관광 통역 안내원', '카지노 딜러', '골프장 캐디', '응원단원', '주방장', '조리사', '요리사', '커피 조리사', '바텐더', '웨이터', '보험 설계사', '텔레마케터', '작물재배 종사자', '양치기', '수렵 종사원', '동물 사육사', '벌목원', '어부', '해녀', '제빵원', '제과원', '도축원', '단조원', '항공기 정비원', '광원', '배관공', '원자력발전장치 운전원', '철도 및 전동차 기관사', '택시 운전원', '버스 운전원', '화물차 및 특수차 운전원', '선박 갑판승무원 및 관련 종사원', '건설 단순 종사원', '배달원', '우편물 집배원', '환경 미화원', '경비원', '가사 도우미', '육아 도우미', '패스트푸드원', '주유원', '전단지 배포원 및 벽보원', '목동', '주차 안내원', '군인', '장교', '장기 부사관', '준위']
        choice = random.choice(job_past)    
        Person.objects.create(name=my_name, past_job=choice)
        person = Person.objects.get(name=my_name)

    context={
        'person' : person,
    }   
    return render(request, 'jobs/past_life.html', context)