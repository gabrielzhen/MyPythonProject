'''
创建35份不同的试卷
每份试卷50道题，随机次序
每道题一个正确答案 三个错误答案 次序随机
35份答案
'''
#todo 创建一个题库字典
import random
capitals={'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#todo 利用文件函数创建文件
for quizNum in range(35):
    #create two files
    quizfile=open('capitalquiz%s.txt'%(quizNum+1),'w')
    answerfile=open('capitalquiz%s_answer.txt'%(quizNum+1),'w')

    #write out the head of the quiz
    quizfile.write('Name:\nDate:\nPeriod:\n')
    quizfile.write((' '*20)+'State Capitals Quiz(From%s)\n\n'%(quizNum+1))
    #random list
    states=list(capitals.keys())
    random.shuffle(states)
#todo 随机生成答案
    for questionNum in range(50):
        #write the quiz file
        correctAnswer=capitals[states[questionNum]]
        wrongAnswer=list(capitals.values())
        wrongAnswer.remove(correctAnswer)
        wrongAnswer=random.sample(wrongAnswer,3)
        answerOption=wrongAnswer+[correctAnswer]
        random.shuffle(answerOption)
        quizfile.write('%s.What is the capital of %s?\n'%(quizNum+1,states[questionNum]))
        for i in range(4):
            quizfile.write('%s.%s\n'%('ABCD'[i],answerOption[i]))
        quizfile.write('\n')
        #write the answer file
        answerfile.write('%s.%s\n'%(quizNum+1,'ABCD'[answerOption.index(correctAnswer)]))
    quizfile.close()
    answerfile.close()
