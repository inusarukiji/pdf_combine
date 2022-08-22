# README
フォルダ内のpdfファイルを結合するソフト<br><br>
  
### **pdf_combine_cui**  
コマンドプロンプト仕様。pythonスクリプトファイルのパスとpdfファイルが格納されたフォルダのパスの２つを引数にとる<br><br>
  
### **pdf_combine_dialog**  
ダイアログ形式のwindowが開くので、そこでpdfファイルが格納されたフォルダを選択する。  
exe版はpyinstallerで実行ファイル化したもので、64bitWindowsで動く。<br><br>

### 注意事項
pdf_cobine_dialogはPyPDF2をimportしているため、ファイルパスに日本語を含むことができない。  
出力結果は指定フォルダ内に"Y年M月D日仮"という名称で作成される。  
ファイルの結合順序は名前の昇順
