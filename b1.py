from bs4 import BeautifulSoup

html_doc="""
<!doctype html><head>
<meta charset=utf-8 />
<link rel=stylesheet type=text/css href=/codingbat.css>
<title>CodingBat payne@mattpayne.org Done Page</title>
<script type='text/javascript'>
var problems = [
{id:'p123384',attempts:[
{d:'20170520-145208z', s:'s8'},]},

{id:'p183592',attempts:[
{d:'20170425-181010z', s:'s7'},]},

{id:'p132118',attempts:[
{d:'20170525-033509z', s:'c2'},{d:'20170525-033527z', s:'t3/8'},{d:'20170525-033538z', s:'t4/8'},{d:'20170525-033619z', s:'t3/8'},{d:'20170525-033637z', s:'t4/8'},{d:'20170525-033724z', s:'t5/8'},{d:'20170525-033859z', s:'t5/8'},{d:'20170525-033948z', s:'s8'},{d:'20170525-232444z', s:'s8'},{d:'20170526-022300z', s:'t6/8'},{d:'20170526-022315z', s:'s8'},]},

{id:'p175762',attempts:[
{d:'20170711-193841z', s:'t2/16to'},{d:'20170711-193901z', s:'t2/16to'},{d:'20170711-193926z', s:'t12/16'},{d:'20170711-194049z', s:'s16'},]},

{id:'p197888',attempts:[
{d:'20160530-233649z', s:'c2'},{d:'20160530-233705z', s:'t2/6'},{d:'20160530-233831z', s:'s6'},]},

{id:'p117630',attempts:[
{d:'20170910-002204z', s:'c2'},{d:'20170910-002212z', s:'s11'},]},

{id:'p146974',attempts:[
{d:'20170611-201400z', s:'c2'},{d:'20170611-201411z', s:'t3/6'},{d:'20170611-201428z', s:'t3/6'},{d:'20170611-201449z', s:'t5/6'},{d:'20170611-201456z', s:'s6'},]},

{id:'p161124',attempts:[
{d:'20170601-023216z', s:'c2'},{d:'20170601-023223z', s:'t10/14'},{d:'20170601-023345z', s:'t0/14'},{d:'20170601-023420z', s:'t0/14'},{d:'20170601-023508z', s:'s14'},]},

{id:'p117665',attempts:[
{d:'20170522-200429z', s:'s10'},]},

{id:'p139586',attempts:[
{d:'20170522-190252z', s:'s8'},]},

{id:'p170181',attempts:[
{d:'20170522-190624z', s:'c2'},{d:'20170522-190631z', s:'s8'},]},

{id:'p181634',attempts:[
{d:'20170522-200534z', s:'s8'},]},

{id:'p177528',attempts:[
{d:'20170522-202843z', s:'s8'},]},

{id:'p103456',attempts:[
{d:'20170601-023541z', s:'s9'},]},

{id:'p124510',attempts:[
{d:'20170601-023636z', s:'s9'},]},

{id:'p137274',attempts:[
{d:'20170601-022324z', s:'s10'},]},

{id:'p105671',attempts:[
{d:'20170601-022604z', s:'s8'},]},

{id:'p194496',attempts:[
{d:'20170601-022419z', s:'c2'},{d:'20170601-022528z', s:'s10'},]},

{id:'p184496',attempts:[
{d:'20170601-022635z', s:'s13'},]},

{id:'p115967',attempts:[
{d:'20170601-023758z', s:'s12'},]},

{id:'p148198',attempts:[
{d:'20170601-023901z', s:'s9'},]},

{id:'p132748',attempts:[
{d:'20170601-023010z', s:'s12'},]},

];

</script>
<script type='text/javascript' src='/protovis-r3.2.js'></script>
<script type='text/javascript' src='/trailgraph.js'></script>
</head><body>
<div style='float:right;  margin:0px; border: 1px solid lightgray;'><table><form  method=post action=/login><tr><td>id/email</td><td><input type=text name=uname size=20></td></tr><tr><td>password</td><td><input type=password name=pw size=20></td></tr><tr><td></td><td><input type=submit name=dologin value='log in'></td></tr> <input type=hidden name=fromurl value='/done'></form><tr><td colspan=2><a href=/reset>forgot password</a> | <a href='/pref?docreate=1'>create account</a></td></tr></div></td></tr></table></div><div  style='float:right'><table><tr><td valign=top style='text-align:right' colspan=1><a href=/about.html>about</a> | <a href=/help.html>help</a> | <a href=/doc/code-help-videos.html>code help+videos | <a href=/done>done</a> | <a href='/pref'>prefs</a> </td></tr></table></div><a href=/><span style='font-size:200%;'>CodingBat</span></a> code practice<h2>CodingBat payne@mattpayne.org Done Page</h2>

<p>Count:22
<form method=post>
<input type=checkbox name=showpg
 checked onclick='this.form.submit();'> Show Progress Graphs &nbsp; <input type=checkbox name=showwarm
 checked onclick='this.form.submit();'> Include Warmup Problems &nbsp; <input type=checkbox name=showstart
 onclick='this.form.submit();'> Include problems started but not yet done</form>
<p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p123384'>Warmup-1 frontBack</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-05-20 14:52:08 GMT</span>
<div><script type='text/javascript'>buildGraph(0);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p183592'>Warmup-1 front22</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-04-25 18:10:10 GMT</span>
<div><script type='text/javascript'>buildGraph(1);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p132118'>String-1 conCat</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-05-26 02:23:15 GMT</span>
<div><script type='text/javascript'>buildGraph(2);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p175762'>String-2 bobThere</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-07-11 19:40:49 GMT</span>
<div><script type='text/javascript'>buildGraph(3);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p197888'>Map-1 mapBully</a> &nbsp;&nbsp;<span style='font-size:x-small'>2016-05-30 23:38:31 GMT</span>
<div><script type='text/javascript'>buildGraph(4);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p117630'>Map-2 wordCount</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-09-10 00:22:12 GMT</span>
<div><script type='text/javascript'>buildGraph(5);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p146974'>AP-1 scoresIncreasing</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-11 20:14:56 GMT</span>
<div><script type='text/javascript'>buildGraph(6);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p161124'>Recursion-1 countAbc</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:35:08 GMT</span>
<div><script type='text/javascript'>buildGraph(7);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p117665'>Functional-1 doubling</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-05-22 20:04:29 GMT</span>
<div><script type='text/javascript'>buildGraph(8);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p139586'>Functional-1 square</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-05-22 19:02:52 GMT</span>
<div><script type='text/javascript'>buildGraph(9);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p170181'>Functional-1 addStar</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-05-22 19:06:31 GMT</span>
<div><script type='text/javascript'>buildGraph(10);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p181634'>Functional-1 copies3</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-05-22 20:05:34 GMT</span>
<div><script type='text/javascript'>buildGraph(11);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p177528'>Functional-1 moreY</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-05-22 20:28:43 GMT</span>
<div><script type='text/javascript'>buildGraph(12);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p103456'>Functional-2 noNeg</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:35:41 GMT</span>
<div><script type='text/javascript'>buildGraph(13);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p124510'>Functional-2 no9</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:36:36 GMT</span>
<div><script type='text/javascript'>buildGraph(14);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p137274'>Functional-2 noTeen</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:23:24 GMT</span>
<div><script type='text/javascript'>buildGraph(15);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p105671'>Functional-2 noZ</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:26:04 GMT</span>
<div><script type='text/javascript'>buildGraph(16);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p194496'>Functional-2 noLong</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:25:28 GMT</span>
<div><script type='text/javascript'>buildGraph(17);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p184496'>Functional-2 no34</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:26:35 GMT</span>
<div><script type='text/javascript'>buildGraph(18);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p115967'>Functional-2 noYY</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:37:58 GMT</span>
<div><script type='text/javascript'>buildGraph(19);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p148198'>Functional-2 two2</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:39:01 GMT</span>
<div><script type='text/javascript'>buildGraph(20);</script></div><p style='margin: 1em 0 0em;' ><img src=/c2.jpg><a href='/prob/p132748'>Functional-2 square56</a> &nbsp;&nbsp;<span style='font-size:x-small'>2017-06-01 02:30:10 GMT</span>
<div><script type='text/javascript'>buildGraph(21);</script></div><p>Count:22
<p><a href=/doc/practice/code-badges.html><b>Code Badge Data</b></a>
<p>&nbsp; Java problems solved by section:
String-1:1&nbsp;Logic-1:0&nbsp;Array-1:0&nbsp;String-2:1&nbsp;Array-2:0&nbsp;<p>&nbsp; Python problems solved by section:
String-1:0&nbsp;Logic-1:0&nbsp;List-1:0&nbsp;String-2:0&nbsp;List-2:0&nbsp;<p><font size='-2'>(request from:23.239.3.90 
2018-03-17 01:06:57 GMT)</font><p class=max>
Use the Teacher Share pref setting to share this page with a teacher. 
This done page also has a fixed url (<a href='/done?user=payne@mattpayne.org&tag=6764324312'>here</a>) which can be sent to anyone so they can see this list of done problems (but not the code).
<p class=max>
<a href=/progress-graphs.html>About progress graphs</a> 
<p style='font-size:x-small;'>Copyright <a style='font-size:x-small;' href='http://www-cs-faculty.stanford.edu/~nick'>Nick Parlante</a> 2017 - <a style='font-size:x-small;' href=/privacy.html>privacy</a>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
#print(soup.script)
a = soup.find_all('a')
print(a[20])
ps = a[20].findPreviousSibling()
print(ps)

