from flask import Flask, render_template, request
from typing import Any
from process import process_answer

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def do_process() -> str:
    res = process_answer(request.form['question'])
    result = res['result']
    return render_template('results.html', the_title='我是数据库问答机器人', 
                           the_question=request.form['question'], the_result=result)


@app.route('/entry')
def entry_page() -> Any:
    return render_template('entry.html', the_title='我是数据库问答机器人')

app.run(port=8080, debug=True)
