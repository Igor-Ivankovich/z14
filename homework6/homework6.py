"""

Написать !консольную! программу, которая на вход получает имя входного файла,
имя выходного и решает определенную задачу.
Задача программы:
1) По расширению файлов определить какой тип данных в них.
 - <file_name>.json - в файле лежит json
 - <file_name>.csv - лежит csv
 - <file_name>.xml - лежит xml
  - <file_name>.bin - лежит объект, упакованный при помощи pickle
2) Перегнать данные из одного файла в другой соблюдая тип данных
Пример:
python homework6.py data.json data.csv
из json который лежит в data.json сделать csv и положить в файл data.csv

PS: для проверки существования файла можно использовать os.path.exists(<path>)
3) Второй файл в аргументе может быть не указан.
python homework6.py data.json

Если второй аргумент не указан, то данные из файла data.json вывести на экран в
виде питоновского объекта.


PS: глубина вложенности данных - 1
т.е. для xml не может быть вложености глубже тегов внутри тега <item>
<root>
   <item>
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications
      with XML.</description>
   </item>
   <item>
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies,
      an evil sorceress, and her own childhood to become queen
      of the world.</description>
   </item>
</root>

для json не могут быть объекты внутри объектов
"""