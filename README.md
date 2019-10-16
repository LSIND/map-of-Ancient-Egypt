# OpenStreetMap of Pyramids of Ancient Egypt

> ### Man fears time, but time fears the Pyramids.

Probably all of you saw maps of Ancient Egyptian sites (I had school workbook) in stylized way like this below:

![Map of Ancient Egypt](https://www.dropbox.com/s/cvhbuugrkstto3b/map-of-ancient-egypt.png?raw=1)

<p align="justify">I wished to recreate this kind of map using Python and OpenStreetMap but the problem I faced was the absolute absence of some dataset or even list with coordinates of egyptian pyramids. So I took different historical sources, Google Maps, wikipedia (in English, French, Deutsch, Russian) and combined the information in one dataset of known pyramids as an .csv file (<a href="https://www.kaggle.com/lsind18/egyptianpyramids">on Kaggle</a> or <a href="https://github.com/LSIND/map-of-Ancient-Egypt/blob/master/pyramids.csv">on GitHub</a>). If you know more information or find some nonconformity - let me know! <b>Such important part of mankind history shouldn't be forgotten.</b></p>

### &#x1F53A; Short (historical mostly) overview of this work.

> Source code uses only 2 modules: [*pandas*](https://pandas.pydata.org) (for dataframes) and [*folium*](https://python-visualization.github.io/folium/) (for interactive maps based on OpenStreetMap).

**1. Install and import modules**

```
pip install pandas
pip install folium
```

**2. Check the [.csv file with pyramids](https://github.com/LSIND/map-of-Ancient-Egypt/blob/master/pyramids.csv):**

 - the file contains 62 Egyptian pyramids;
 - every pyramid has a *Modern Name* and some of them have an *Ancient Name* as it was translated from ancient egyptian hieroglyphs;
 - every pyramid has its coordinates - *Latitude* and *Longitude* in decimal form;
 - there are owners of a pyramid and sometimes supposed owners - symbol '**(?)**' follows the name of *Pharaoh*;
 - every pyramid is marked with it's *Dynasty* and location (*Site*);
 - there is missing data (*Slope* and *Volume* of some pyramids mostly);
 - base (*Base1 (m)* and *Base2 (m)*) and *Height (m)* of pyramid are in meters and represent the original size (that the pyramid was or was supposed to be);
 - some pyramids are marked with a [*Lepsius* number](https://en.wikipedia.org/wiki/Lepsius_list_of_pyramids) which is a roman number from I to LXVII plus the pyramid number LG100 (pyramid of Khentkaus I);
 - most pyramids have a *Type* of construction (Step, True, Smooth-faced, Smooth-sided) and most used *Material* (Limestone, Mudbrick, Granite, Sandstone or a combination);
 - there is also a column *Comment* which contains some descriptive information.

 
 **3. Get some statistics:**
- maximum height of pyramid is 146.6 meters (Great Pyramid of Giza) and minimum - 6.8 meters (Pyramid of Seila).

**4. Arrange pyramids into periods:**
> <p align="justify"><i>I am taking in consideration only Early Dynastic Period, Old Kingdom, FIP, Middle Kingdom, SIP and the beginning of New Kingdom.</i></p>

<table class="tg">
  <tr>
    <th class="tg-7p3h"></th>
    <th class="tg-7p3h"><sup>Period</sup></th>
    <th class="tg-7p3h"><sup>Years (approx.)</sup></th>
    <th class="tg-7p3h"><sup>Dynasties</sup></th>
  </tr>
  <tr>
    <td class="tg-7p3h"><sup>1</sup></td>
    <td class="tg-7p3h"><sup>Early Dynastic Period</sup></td>
    <td class="tg-7p3h"><sup>c. 3150 BC – c. 2686 BC</sup></td>
    <td class="tg-7p3h"><sup>1. First Dynasty of Egypt (ca. 3100 BC – ca. 2900 BC)<br>2. Second Dynasty of Egypt (c. 2890 BC – c. 2686 BC)</sup></td>
  </tr>
  <tr>
    <td class="tg-7p3h"><sup>2</sup></td>
    <td class="tg-7p3h"><sup>Old Kingdom<br><i>Age of the Pyramids</i></sup></td>
    <td class="tg-7p3h"><sup>c. 2686 BC – c. 2181 BC</sup></td>
    <td class="tg-7p3h"><sup>3. Third Dynasty of Egypt (ca. 2686 BC – ca. 2613 BC)<br>4. Fourth Dynasty of Egypt (ca. 2613 BC – ca. 2494 BC)<br>5. Fifth Dynasty of Egypt (ca. 2494 BC – ca. 2345 BC)<br>6. Sixth Dynasty of Egypt (ca. 2345 BC – ca. 2181 BC)<br><i> - Seventh Dynasty of Egypt is considered spurious</sup></td>
  </tr>
  <tr>
    <td class="tg-7p3h"><sup>3</sup></td>
    <td class="tg-7p3h"><sup>First Intermediate<br>Period (FIP)<br><i>Dark age</i></sup></td>
    <td class="tg-7p3h"><sup>c. 2181 BC – c. 2055 BC</sup></td>
    <td class="tg-7p3h"><sup>8. Eight Dynasty of Egypt (ca. 2181 BC – ca. 2160 BC)<br>9. Ninth Dynasty of Egypt (ca. 2160 BC – ca. 2130 BC)<br>10. Tenth Dynasty of Egypt (ca. 2130 BC – ca. 2040 BC)<br><i> - these dynasties are often combined</i></sup></td>
  </tr>
  <tr>
    <td class="tg-8hko"><sup>4</sup></td>
    <td class="tg-8hko"><sup>Middle Kingdom<br><i>Reunification</i></sup></td>
    <td class="tg-8hko"><sup>c. 2055 BC – c. 1650 BC</sup></td>
    <td class="tg-8hko"><sup>11. Eleventh Dynasty of Egypt (ca. 2130 BC – ca. 1991 BC)<br>12. Twelfth Dynasty of Egypt (1991 BC – 1802 BC)<br>13. Thirteenth Dynasty of Egypt (1803 BC – 1649 BC)<br>14. Fourteenth Dynasty of Egypt (ca. 1725 BC – ca. 1650 BC)<br><i>- these dynasties are often combined under the group title <br> Middle Kingdom</i></sup></td>
  </tr>
  <tr>
    <td class="tg-8hko"><sup>5</sup></td>
    <td class="tg-8hko"><sup>Second Intermediate<br>Period (SIP)</sup></td>
    <td class="tg-8hko"><sup>c. 1650 BC – c. 1550 BC</sup></td>
    <td class="tg-8hko"><sup>15. Fifteenth Dynasty of Egypt (1650 BC – ca. 1550 BC)<br>16. Sixteenth Dynasty of Egypt (1649 BC – 1582 BC)<br>17. Seventeenth Dynasty of Egypt (ca. 1580 BC – ca. 1550 BC)</sup></td>
  </tr>
  <tr>
    <td class="tg-8hko"><sup>6</sup></td>
    <td class="tg-8hko"><sup>New Kingdom<br><i>Egyptian Empire</i></sup></td>
    <td class="tg-8hko"><sup>c. 1550 BC – c. 1069 BC</sup></td>
    <td class="tg-8hko"><sup>18. Eighteenth Dynasty of Egypt (1550 BC – 1292 BC)</sup></td>
  </tr>
</table>
</sup>

**5. Some preparations before creating marks on the map:**
  - find mean latitude and longitude of dataset;
  - create function to color different kingdoms;
  - provide a legend.
  
  **6. Сreating a map**

![Map with known pyramids](https://www.dropbox.com/s/q6xy1v8ionlny74/map1.JPG?raw=1)

### :earth_africa: View in browser: [OpenStreetMap of 62 pyramids](https://lsind.github.io/map-of-Ancient-Egypt/map-pyramids.html)

   - glyphicon with open eye shows if Pharaoh' name is certain
   - popup shows the modern name of pyramid

**7. Create [Lepsius list](https://en.wikipedia.org/wiki/Lepsius_list_of_pyramids) and map**

- Drop rows where Lepsius column contains NaN values 
- Create Lepsius map: zoom in to get the pyramids and the Pharaoh's name

![Lepsius Map](https://www.dropbox.com/s/fs0qougstmvdkow/mapL.JPG?raw=1)


### :earth_africa: View in browser: [OpenStreetMap of Lepsius list](https://lsind.github.io/map-of-Ancient-Egypt/map-lepsius.html)

   - red circle represents a pyramid with a roman number in it; zoom in!
   - popup shows the owner's (pharaoh or his wife) name

------------------------------

### :small_red_triangle: The interactive maps in my [Kaggle notebook](https://www.kaggle.com/lsind18/pyramids-of-ancient-egypt-on-a-map)

### :page_facing_up:  Source code on GitHub [.py and .ipynb](https://github.com/LSIND/map-of-Ancient-Egypt/tree/master/source)

P.S. Feel free to contact me if you have some additional info about [Egyptian pyramids dataset](https://www.kaggle.com/lsind18/egyptianpyramids).
