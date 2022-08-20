# pdf_combine

フォルダ内のpdfファイルを結合するソフト  
  
### **pdf_combine_cui**  
コマンドプロンプトでpythonスクリプトファイルのパスとpdfファイルが格納されたフォルダのパスの２つを引数にとる  
### **pdf_combine_dialog**  
ダイアログ形式のwindowが開くのでそこでpdfファイルが格納されたフォルダを選択する  
exe版はpyinstallerで実行ファイル化したもので、64bitWindowsで動く。  

### 注意事項
pdf_cobine_dialogはPyPDF2をimportしているため、ファイルパスに日本語を含むことができない
