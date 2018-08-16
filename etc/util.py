""" function """
# 엑셀 데이터 export
import xlsxwriter
def export_date_excel(request):
    dataF = request
    filename = 'hk_result(href).xlsx'
    dataF.to_excel(filename,'Sheet1',index=False, engine='xlsxwriter')
export_date_excel

# warning 메시지 무시 : ignore annoying warning (from sklearn and seaborn)
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn


""" 기타 """
# csv 데이터 export '''
DataFrame.to_csv('파일명', sep='\t', encoding='utf-8', index=False)

# 출력 소수점 3자리 까지 제한
pd.set_option('display.float_format', lambda x: '{:.3f}'.format(x))


""" DataFrame """
# categorical variable => dummy로 변환
df_train = pd.get_dummies(df_train)

# NA 제거
frame = frame.dropna()

# 중복제거
frame = frame.drop_duplicates()

# 'javascript'로 시작하는 데이터 제거
frame = frame[~frame['href'].str.startswith('javascript')]

# /~~~로 시작하는 href에 domain 추가
frame = frame['href'].replace(regex = ['^//'], value = 'https://')
# 주의 : 결과 Serise

# 신규 열 추가 => 하나의 값(str)을 row갯수 만큼 채우기
filter_cookie.loc[:, '_id'] = np.array(_id * len(filter_cookie))

# 특정 값이 존재하는 row 필터 => 'name' 열에서 4개 데이터 포함하는 row만 추출
filter_cookie = filter_cookie[filter_cookie['name'].isin(['menuId',  'menuLoginId',  'checkMenuId',  'searchMenuId'])]

# Dataframe pivoting => _id를 기준
frame = frame.pivot(index = '_id', columns = 'name', values = 'value')

# 특정열 데이터 타입 변경하기
temp['_id'] = temp['_id'].astype(str)


""" Series """
# /~~~로 시작하는 href에 domain 추가
frame = frame.str.replace('^/', domain)

# html문법기호 삭제
frame = frame.str.replace('\n|\t', '')

# http -> https
frame = frame.str.replace('^http://', "https://")

# domain : https://www.uplus.co.kr 가 존재하는 문자열만 추출
frame = frame.loc[frame.str.contains('https://www.uplus.co.kr/')]

# index 초기화
frame = frame.reset_index(drop = True)
frame = frame.get_values().tolist()


""" Crawling """
# newwork log 추출용
# - 자바스크립트 로딩하기
caps = webdriver.DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}
