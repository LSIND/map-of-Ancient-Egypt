# OpenStreetMap of Pyramids of Ancient Egypt

## From Papyrus to Pixels: Building an Interactive Map of Egyptian Pyramids with OpenStreetMap

> Man fears time, but time fears the Pyramids.

Most people are familiar with those stylized maps of ancient Egyptian sites you often see in school workbooks. Inspired by that style, this project set out to create a similar map using Python and OpenStreetMap. But the main problem was that there was no ready-made dataset /or even a simple list/ of the geographic coordinates of Egyptian pyramids.

![Map of Ancient Egypt](https://www.dropbox.com/s/cvhbuugrkstto3b/map-of-ancient-egypt.png?raw=1)

To fill that gap, I pulled together information from a bunch of different places: historical sources, Google Maps, and various research papers in English, French, German, Dutch, and Russian. The result is a CSV file with 62 documented pyramids (you can find it on [Kaggle](https://www.kaggle.com/lsind18/egyptianpyramids) or [GitHub](https://github.com/LSIND/map-of-Ancient-Egypt/blob/master/pyramids.csv)). For each pyramid, the file gives the modern name, plus the ancient name if we have a hieroglyphic transliteration. The coordinates are in decimal degrees. You'll also see who the pyramid is attributed to (if there's any doubt, it's marked with a "(?)") along with the dynasty and location.

If you know more or spot something that doesn't match up, let me know! **Such important part of mankind history shouldn't be forgotten.**

## Dataset Structure

The accompanying CSV file comprises 62 records of Egyptian pyramids and adheres to the following schema:
- Nomenclature: Each pyramid is identified by a Modern Name. Where transliterations from ancient Egyptian hieroglyphs are available, the corresponding Ancient Name is also provided.
- Geospatial Data: Geographic coordinates (Latitude and Longitude) are supplied for all 62 entries in decimal degrees.
- Attribution: The Owner field denotes the ruler associated with the structure. In cases of scholarly uncertainty, a "(?)" symbol follows the ruler's name. All entries include a Dynasty and a Site (location) designation.
- Physical Dimensions: The original (intended or actual) dimensions of the pyramids are recorded. This includes the base lengths (Base1 (m) and Base2 (m)) and the Height (m), all expressed in meters.
- Lepsius Classification: Some pyramids are identified by their Lepsius number, presented as a Roman numeral (I to LXVII), in addition to the distinct identifier LG100 for the pyramid of Khentkaus I.
- Typology and Materials: The construction Type (e.g., Step, True, Smooth-faced) and primary building Material (e.g., Limestone, Mudbrick, Granite, Sandstone, or combinations thereof) are specified for the majority of entries.
- Supplementary Notes: A Comment field is included to provide additional descriptive or contextual information.
- Data Completeness: Certain entries contain gaps, most frequently in the fields for Slope and Volume.

## Chronological Classification of the Pyramids
> <p align="justify"><i>For the purposes of this analysis, the pyramids are classified according to the standard chronological framework of ancient Egyptian history, encompassing the Early Dynastic Period through the beginning of the New Kingdom. The dynasties are enumerated following conventional Egyptological chronology.</i></p>

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

## Cartographic Methodology
  - The interactive map was generated using the Folium library.
  - The mean geographic coordinates of the dataset were calculated to establish an optimal initial viewport.
  - For each pyramid in the dataset, a circular marker was placed at its corresponding coordinates.
  - To enable period-based visualization, a classification scheme was implemented mapping dynasties to historical periods:

| Period                     | Abbreviation | Dynasties | Color  |
|----------------------------|--------------|-----------|--------|
| Early Dynastic Period      | EDP          | 1-2       | <span style="color:violet;">Violet</span> |
| Old Kingdom                | Old          | 3-7       | <span style="color:green;">Green</span>  |
| First Intermediate Period  | FIP          | 8-10      | <span style="color:blue;">Blue</span>  |
| Middle Kingdom             | Middle       | 11-14     | <span style="color:orange;">Orange</span> |
| Second Intermediate Period | SIP          | 15-17     | <span style="color:yellow;">Yellow</span> |
| New Kingdom                | New          | 18        | <span style="color:red;">Red</span>    |

  
## Interactive Map

![Map with known pyramids](https://www.dropbox.com/s/q6xy1v8ionlny74/map1.JPG?raw=1)

### :earth_africa: View in browser: [OpenStreetMap of 62 pyramids](https://lsind.github.io/map-of-Ancient-Egypt/map-pyramids.html)
- Color coding: Pyramids are colored according to their historical period (Early Dynastic, Old Kingdom, etc.) as defined in Section 4, facilitating immediate chronological identification.
- Glyphicon indicators: The use of open/closed eye icons provides a visual cue for the level of scholarly certainty regarding royal attribution:
    - Eye-open (👁️): Pharaoh attribution is confirmed
    - Eye-close: Pharaoh attribution is conjectural (indicated by "?" in the dataset)
- Popup information: Clicking on any marker reveals the pyramid's modern name, enabling quick identification without visual clutter.

## Lepsius List Visualization
The Lepsius list, a seminal 19th-century catalog of Egyptian pyramids compiled by Karl Richard Lepsius, was isolated from the main dataset by filtering for entries with assigned Lepsius numbers.

![Lepsius Map](https://www.dropbox.com/s/fs0qougstmvdkow/mapL.JPG?raw=1)

### :earth_africa: View in browser: [OpenStreetMap of Lepsius list](https://lsind.github.io/map-of-Ancient-Egypt/map-Lepsius.html)
- Circular markers: Red circles provide high visibility against the terrain base layer
- Roman numeral identifiers: Hover tooltips display the Lepsius number (I-LXVII) for immediate catalog reference
- Ruler attribution popups: Clicking reveals the associated pharaoh or royal consort
- Zoom-dependent detail: The higher zoom level (10) enables examination of spatial relationships between pyramids at individual sites

------------------------------

### &#x1F53A; The interactive maps in my [Kaggle notebook](https://www.kaggle.com/lsind18/pyramids-of-ancient-egypt-on-a-map)

P.S. Feel free to contact me if you have some additional info about [Egyptian pyramids dataset](https://www.kaggle.com/lsind18/egyptianpyramids).
