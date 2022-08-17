from flask import Flask, render_template,request,current_app
import os 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('01.index.html')


@app.route("/menu", methods=['GET','POST'])
def meSnu():
     if request.method == 'GET':
        languages = [
            {'disp':'영어','value':'en'},
            {'disp':'일어','value':'js'},
            {'disp':'중국어','value':'cn'},
            {'disp':'프랑스어','value':'fr'},
            {'disp':'스페인어','value':'es'}
        ]
        return render_template('02.Menu.html', options=languages)
     else:
        # 사용자가 입력한 정보를 서버가 읽기
        index = request.form['index']
        lang = request.form['lang']
        lyrics = request.form['lyrics']
        print(lang,'\n',index,'\n',lyrics, sep='')
        #사용자가 입력한 파일을 읽어서 upload 디렉토리에 저장
        f_image= request.files['image']
        print(f_image.filename)     #사용자가 입력한 파일 이름
        filename = os.path.join(current_app.root_path, 'static/upload/') + f_image.filename
        print(filename)
        f_image.save(filename)
        #모델 실행후 결과를 돌려줌
        result = '독술독술 (73.52%)'       
        return render_template('03.Menu_res.html', result=result, fname=f_image.filename)

if __name__ == '__main__':
    app.run(debug=True)