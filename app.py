{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red24\green24\blue24;\red193\green193\blue193;
\red202\green202\blue202;\red140\green211\blue254;\red212\green214\blue154;\red194\green126\blue101;\red70\green137\blue204;
}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c12157\c12157\c12157;\cssrgb\c80000\c80000\c80000;
\cssrgb\c83137\c83137\c83137;\cssrgb\c61176\c86275\c99608;\cssrgb\c86275\c86275\c66667;\cssrgb\c80784\c56863\c47059;\cssrgb\c33725\c61176\c83922;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf4 \strokec4  flask \cf2 \strokec2 import\cf4 \strokec4  Flask, render_template\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 app \cf5 \strokec5 =\cf4 \strokec4  Flask(\cf6 \strokec6 __name__\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 @app.route\cf4 \strokec4 (\cf8 \strokec8 '/'\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 def\cf4 \strokec4  \cf7 \strokec7 index\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 return\cf4 \strokec4  render_template(\cf8 \strokec8 'index.html'\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf6 \strokec6 __name__\cf4 \strokec4  \cf5 \strokec5 ==\cf4 \strokec4  \cf8 \strokec8 '__main__'\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     app.run(\cf6 \strokec6 debug\cf5 \strokec5 =\cf9 \strokec9 True\cf4 \strokec4 )\cb1 \
}