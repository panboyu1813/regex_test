@app.route('/test_tool', methods=['GET', 'POST'])
def test_tool():
    result = ""
    regex = ""
    accept = ""
    reject = ""

    if request.method == 'POST':
        regex = request.form.get('regex', '')
        accept = request.form.get('accept', '')
        reject = request.form.get('reject', '')
        try:
            pattern = re.compile(f"^{regex}$")
            for line in accept.strip().splitlines():
                if not pattern.fullmatch(line.strip()):
                    result += f"❌ Accept 失敗：應該要匹配 → 「{line.strip()}」\\n"
            for line in reject.strip().splitlines():
                if pattern.fullmatch(line.strip()):
                    result += f"❌ Reject 失敗：不應該匹配 → 「{line.strip()}」\\n"
            if not result:
                result = "✅ 全部通過！"
        except re.error as e:
            result = f"❌ 無效的正則表達式：{str(e)}"

    return render_template('test_tool.html', regex=regex, accept=accept, reject=reject, result=result)
