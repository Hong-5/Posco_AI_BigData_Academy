#!/usr/bin/env python
# coding: utf-8

# # 0-1. 학점 생성 함수
# 
# - 평균성적을 받아서 grade 리턴

# In[65]:


def make_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'


# # 0-2. 출력 함수

# ## 0-2-1) hearder 출력 함수

# In[66]:


def print_header():
    strFormat = '%15s%15s%15s%15s%15s%15s\n'
    strOut = ''
    strOut += strFormat % ('Student','Name','Midterm', 'Final', 'Average', 'Grade')
    strOut += '-'*90 ### ---- 밑에 한 줄을 띄우지 않기 위해 /n을 할 필요가 없어 따로 더해줌
    print(strOut)


# ## 0-2-2) 학생정보 출력 함수

# In[67]:


def print_stu_info(stu_list):
    strFormat = '%15s%15s%15s%15s%15s%15s\n'
    strOut = f''
    for i in stu_list:
        ## 평균점수는 소수점 첫째자리까지만 출력
        strOut += strFormat %(i, stu_list[i][0], int(stu_list[i][1]), int(stu_list[i][2]), format(float(stu_list[i][3]), '.1f'), stu_list[i][4])
    print(strOut)


# # 0-3. 성적 기준 정렬

# In[68]:


def sort_by_ave(x):
    sort_dict = dict(sorted(x.items(), key=lambda x: x[1][3], reverse = True))
    return sort_dict


# # 1. show (전체 학생 정보 출력)

# In[69]:


def show():
    # 딕셔너리 정렬
    sort_by_av_list = sort_by_ave(stu_data)
    print_header()
    print_stu_info(sort_by_av_list)


# # 2. search (특정 학생 검색)

# In[70]:


def search():    
    search_stu = str(input('Student ID: '))

    if search_stu not in stu_data:
        print('NO SUCH PERSON.')
    else:
        new_dic = {key: value for key, value in stu_data.items() if key == search_stu}
        print_header()
        print_stu_info(new_dic)


# # 3. changescore (점수 수정)

# In[71]:


def changescore():
    global stu_data
    
    # search 함수 실행
    search_stu = str(input('Student ID: '))

    if search_stu not in stu_data:
        print('NO SUCH PERSON.')
    else:
        new_dic = {key: value for key, value in stu_data.items() if key == search_stu}
        test_when = input('Mid/Final? ')
        if test_when in ['mid', 'final']:
            new_score = int(input('Input new score: '))
            if 0 <= new_score and new_score <= 100:
                ## 찾은 학생의 변경 이전 정보 출력
                print_header()
                print_stu_info(new_dic)
                print('Score changed.')
                
                
                ## new_dict의 값 변경
                if test_when == 'mid':
                    stu_data[search_stu][1] = new_score
                    stu_data[search_stu][3] = (stu_data[search_stu][1] + stu_data[search_stu][2]) / 2
                    stu_data[search_stu][4] = make_grade(stu_data[search_stu][3])
                    
                    
                else:
                    stu_data[search_stu][2] = new_score
                    stu_data[search_stu][3] = (stu_data[search_stu][1] + stu_data[search_stu][2]) / 2
                    stu_data[search_stu][4] = make_grade(new_dic[search_stu][3])
                    
                    
                
                ## 찾은 학생의 변경 이후 정보 출력
                new_dic = {key: value for key, value in stu_data.items() if key == search_stu}
                print_header()
                print_stu_info(new_dic)
                


# # 4. add (학생 추가)

# In[72]:


def add():
    global stu_data
    
    new_stu_id = str(input('Student ID: '))

    if new_stu_id in stu_data:
        print('ALREADY EXISTS.')
    else:
        new_stu_name = str(input('Name: '))
        new_mid_score = int(input('Midterm Score: '))
        if 0 > new_mid_score or new_mid_score > 100:
            print('유효한 성적의 범위가 아닙니다.')
        else:
            new_fin_score = int(input('Final Score: '))
            if 0 > new_fin_score or new_fin_score > 100:
                print('유효한 성적의 범위가 아닙니다.')
            else:
                new_av_score = (new_mid_score + new_fin_score) / 2 # 평균 성적
                new_std_grade = make_grade(new_av_score)

                stu_data[new_stu_id] = [new_stu_name, new_mid_score, new_fin_score, new_av_score, new_std_grade]
        
                print('Student added.')


# # 5. searchgrade (Grade 검색)

# In[73]:


def searchgrade():
    wonder_grade = str(input('Grade to search: '))

    if wonder_grade not in ['A', 'B', 'C', 'D', 'F']:
        pass
    else:
        search_for_grade = []
        new_dic = {key: value for key, value in stu_data.items() if value[4] == wonder_grade}
        if len(new_dic) == 0:
            print('NO RESULTS.')
        else:
            new_dic = sort_by_ave(new_dic)
            print_header()
            print_stu_info(new_dic)


# # 6. REMOVE (특정 학생 삭제)

# In[74]:


def remove_stu():
    global stu_data
    
    if len(stu_data) == 0:
        pass
    else:
        remove_stu_num = str(input('Student ID: '))
        if remove_stu_num not in stu_data.keys():
            print('NO SUCH PERSON.')
        else:
            del stu_data[remove_stu_num]
            print('Student removed.')


# # 7. quit (종료)

# In[75]:


def quit():
    save_or_not = input('Save data?[yes/no] ')
    
    if save_or_not == 'yes':
        save_file_name = input('File name: ')
        
        final_data = sort_by_ave(stu_data)
        
        f = open(save_file_name, 'w')
        for i in final_data:
            line = i + '\t' + str(final_data[i][0]) + '\t' + str(final_data[i][1]) + '\t' + str(final_data[i][2]) + '\n'
            f.write(line)
        f.close()


# # 프로그램 실행

# ## 1) 학생 정보 딕셔너리 생성

# In[76]:


import sys

while True:
    try:
        if len(sys.argv) != 2:
            text_1 = 'students.txt'
        else:
            text_1 = sys.argv[1]

        fr = open(text_1, 'r')
        text = ''

        for txt in fr:
            text += txt
        if text[-1:] == '\n':  # txt파일에 마지막 한줄에 아무것도 없을 때
            text = text[:-1]
    except:
        continue

    

    
    
# 0-2. 학생 딕셔너리 생성 및 값 저장

stu_data = {}

txt_split_n = text.split('\n')
    
for txt in txt_split_n:
    txt_split_t = txt.split('\t') ## 각 \n으로 split한 줄들을 다시 \t로 split
    
    ## 위에서 나눈 리스틍 인덱스로 접근하여 변수 생성 후 딕셔너리에 알맞는 값을 넣어줌
    std_id = str(txt_split_t[0]) # 학번
    std_name = txt_split_t[1] # 이름
    mid_score = int(txt_split_t[2]) # 중간고사 성적
    final_score = int(txt_split_t[3]) # 기말고사 성적
    av_score = (mid_score + final_score) / 2 # 평균 성적
    std_grade = make_grade(av_score) # 학점
    
    stu_data[std_id] = [std_name, mid_score, final_score, av_score, std_grade]


# ## 2) 명령어 입력

# In[56]:


show()

while True:
    
    input_func = input('# ', ).lower() # 입력의 포멧이 대소문자 구분 없기 때문에 input_func ==> lower처리 해서 비교
    
    if input_func == 'show':
        show()
        print()
    elif input_func == 'search':
        search()
        print()
    elif input_func == 'changescore':
        changescore()
        print()
    elif input_func == 'add':
        add()
        print()
    elif input_func == 'searchgrade':
        searchgrade()
        print()
    elif input_func == 'remove':
        remove_stu()
        print()
    elif input_func == 'quit':
        quit()
        break
    else:
        pass


# In[ ]:




