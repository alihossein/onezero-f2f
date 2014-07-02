onezero-f2f
===========

Farsi to Finglish converter uses vowel represenations (in Persian) from Dehkhoda dictionary (www.loghatnaameh.com) and fa.wiktionary.org (currently as backup) and guesses better translations using google suggestions.
This project comes self contained with bs4 (BeautifulSoup4) and requests python libraries.
The application is a django application file which uses translator.py to translate Farsi to Finglish.
Static database for already translated words are stored in worddb.xml
After installing this application on your django server, you can see the translation of words from your django url using GET request with word=[word in Persian] which [word in Persian] is the word that you want to translate to Finglish in Farsi.
You can see a AJAX based preview of this API usage in http://www.onezero.ir/f2fconverter/ or the server with latest working version of this API in http://www.onezero.ir/f2f/?word=%D9%81%D8%A7%D8%B1%D8%B3%DB%8C
Any kind of contribution to this project is most welcome.
There's a plugin for chrome in https://chrome.google.com/webstore/detail/farsi2finglish-translator/fjgndmomllkaoodpcclfeiamjbcncbmc which you can use to select words in Persian and look for the Finglish translation in your browser (special thanks to Garret Verstegen).
