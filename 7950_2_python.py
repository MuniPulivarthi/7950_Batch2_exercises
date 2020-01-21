#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


Sale=pd.read_excel('SaleData.xlsx')


# In[4]:


#Sale.head(5)


# In[5]:


#Question1:
def least_sales(Sale):
    ls=Sale.groupby(['Item'])['Sale_amt'].min().reset_index()
    return ls
least_sales(Sale)


# In[5]:


#Question2:
def sales_year_region(Sale):
    Sale['OrderDate']=pd.to_datetime(Sale['OrderDate'])
    Sale['year'], Sale['month'] = Sale['OrderDate'].dt.year, Sale['OrderDate'].dt.month
    ls=Sale.groupby(['Region','year'])['Sale_amt'].sum().reset_index()
    return ls
sales_year_region(Sale)


# In[6]:


#Question3:
def days_diff(Sale):
    ref_date='2019-03-12'
    ref_date=pd.to_datetime(ref_date)
    Sale['daysdiff']=Sale['OrderDate']-ref_date
    Sale['daysdiff']=abs(Sale['daysdiff'])
    return Sale
days_diff(Sale)


# In[7]:


#Question4:
def mgr_slsmn(Sale):
    Sale['list_of_SalesMen']=Sale['SalesMan']
    s1=Sale.groupby(['Manager'])['list_of_SalesMen'].unique()
    new=pd.DataFrame(s1)
    return new
mgr_slsmn(Sale)


# In[8]:


#Question5:
def slsmn_units(Sale):
    Sale['total_sales']=Sale['Sale_amt']
    s1=Sale.groupby(['Region'])['total_sales'].sum().reset_index()
    Sale['Salesmen_count']=Sale['SalesMan']
    s2=Sale.groupby(['Region'])['Salesmen_count'].nunique().reset_index()
    s3=pd.merge(s1,s2,how='inner',on='Region')
    return s3
slsmn_units(Sale)


# In[9]:


#Question6:
def sales_pct(Sale):
    Sale['percent_sales']=Sale['Sale_amt']
    tot_s1=Sale['Sale_amt'].sum()
    s1=Sale.groupby(['Manager'])['percent_sales'].sum()
    s2=(s1/tot_s1)*100
    new=pd.DataFrame(s2)
    return new
sales_pct(Sale)


# In[11]:


#imdb dataset
imdb = pd.read_csv('imdb.csv', escapechar='\\')
#imdb.head()


# In[12]:


#Question7
def fifth_movie(imdb):
    imdb1=imdb.iloc[4]['imdbRating']
    return imdb1
fifth_movie(imdb)


# In[13]:


#Question8:
def movies(imdb):
    index1=imdb['duration'].idxmin()
    row1=imdb.loc[index1]
    print('Movie with minimum duration is:')
    print(row1['title'])

    index2=imdb['duration'].idxmax()
    row2=imdb.loc[index2]
    print('Movie with minimum duration is:')
    print(row2['title'])
movies(imdb)


# In[14]:


#Question9:
def sort_df(imdb):
    ls=imdb.sort_values(['year','imdbRating'],ascending=[True,False])
    return ls
sort_df(imdb)


# In[48]:


lll1=pd.read_csv('movie_metadata.csv')


# In[51]:


#Question10:
def subset_df(imdb):
    s1=imdb[(imdb['duration']>=30) & (imdb['duration']<=180) & (imdb['gross']>2000000) & (imdb['budget']<1000000)]['movie_title'].reset_index()
    return s1
subset_df(lll1)


# In[16]:


#DIAMONDS DATASET
diamonds=pd.read_csv('diamonds.csv')


# In[17]:


#Question11:
def dupl_rows(diamonds):
    duprows=diamonds[diamonds.duplicated()]
    print(len(duprows))
dupl_rows(diamonds)


# In[18]:


#Question12:
def drop_row(diamonds):
    d1=diamonds[['carat','cut']].dropna()
    return d1
drop_row(diamonds)


# In[19]:


#Question13:
def sub_numeric(diamonds):
    d1=diamonds.select_dtypes(include='number')
    return d1
sub_numeric(diamonds)


# In[22]:


#Question 14
d1=diamonds.copy()
d1=d1.dropna()
d1=d1[d1['z']!='None']
d1['z_new'] = d1['z'].astype(float)
def volume(depth,x,y,z):
    if depth > 60:
        volume=x*y*z
    else:
        volume=8
    return volume
d1['volume']=np.vectorize(volume)(d1['depth'],d1['x'],d1['y'],d1['z_new'])
print(pd.DataFrame(d1))


# In[23]:


#Question15
def impute(diamonds):
    diamonds['price'].fillna(value=diamonds['price'].mean()).reset_index()
    return diamonds
impute(diamonds)


# In[24]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[25]:


imdb=pd.read_csv('imdb (1).csv',escapechar='\\')


# In[26]:


#QUESTION 16:
def get_name(row):
    list1=[]
    for c in imdb1.columns:
        if row[c]==1:             
            list1.append(c)
    return set(list1)
imdb1=imdb[['Action','Adult','Adventure','Animation','Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','FilmNoir','GameShow','History','Horror','Music','Musical','Mystery','News','RealityTV','Romance','SciFi','Short','Sport','TalkShow','Thriller','War','Western'
]].copy()
imdb['Genre']=imdb1.apply(get_name,axis=1)
imdb_final=imdb.groupby(['year','type'])['Genre'].apply(list).reset_index(name='Genre_combo')
imdb_finall=imdb_final.copy()
def function1(list3):
    flat_list = [item for sublist in list3 for item in sublist]    
    return list(set(flat_list))
imdb_finall['Genre_combo1']=imdb_finall['Genre_combo'].apply(function1)
imdb_finall.drop('Genre_combo',axis=1,inplace=True)
d = {'imdbRating': ['min', 'max','mean'], 'duration': ['sum']}
res = imdb.groupby(['year','type']).agg(d)
res.columns = ['_'.join(col) for col in res.columns.values]
res=pd.DataFrame(res)
res
om=pd.merge(imdb_finall,res,how='inner',on=['year','type'])
print(om)


# In[27]:


#QUESTION 17:
#A)Relation betweeb title length and imdb rating
imdb['title_len'] = imdb['title'].apply(len)
correlation=imdb[imdb['type']=='video.movie']['title_len'].corr(imdb['imdbRating'])
print("correlation is",correlation)


# In[29]:


#QUESTION 17
#B)
Quantile1=np.percentile(imdb['title_len'],25)
Quantile2=np.percentile(imdb['title_len'],50)
Quantile3=np.percentile(imdb['title_len'],75)
d1 = {'title_len': ['min', 'max']}
res1 = imdb.groupby(['year']).agg(d1)
res1.columns = ['_'.join(col) for col in res1.columns.values]
res1=pd.DataFrame(res1)
l1=imdb[imdb['title_len']<Quantile1]
l1=l1.groupby(['year'])['type'].count().reset_index()
l1['no_of_videos_less_than_25Percentile']=l1['type']
lxx=l1.drop('type',axis=1)

l2=imdb[(imdb['title_len']>=Quantile1) & (imdb['title_len']<Quantile2)]
l2=l2.groupby(['year'])['type'].count().reset_index()
l2['no_of_videos_25_t0_50Percentile']=l2['type']


l2=pd.DataFrame(l2)
l2=pd.merge(l1,l2,how='outer',on='year')


l3=imdb[(imdb['title_len']>=Quantile2) & (imdb['title_len']<Quantile3)]
l3=l3.groupby(['year'])['type'].count().reset_index()
l3['no_of_videos_50_t0_75Percentile']=l3['type']
l3=pd.DataFrame(l3)
l3=pd.merge(l2,l3,how='outer',on='year')
l3

l4=imdb[(imdb['title_len']>=Quantile3)]
l4=l4.groupby(['year'])['type'].count().reset_index()
l4['no_of_videos_greater_than_75Percentile']=l4['type']
l4=pd.DataFrame(l4)
l4=pd.merge(l3,l4,how='outer',on='year')
l4.sort_values('year')

lxx=l4[['year','no_of_videos_less_than_25Percentile','no_of_videos_25_t0_50Percentile','no_of_videos_50_t0_75Percentile','no_of_videos_greater_than_75Percentile']].copy()
lxx=lxx.sort_values('year')
lxxx=pd.merge(res1,lxx,how='inner',on='year')
lxxx= lxxx.fillna(0)
print(lxxx)


# In[30]:


#print(Quantile3)
def names(a):
    if(a<Quantile1):
        q='Quantile1'
    elif((a>=Quantile1) and (a<Quantile2)):
        q='Quantile2'
    elif((a>=Quantile2) and (a<Quantile3)):
        q='Quantile3'
    else:
        q='Quantile4'
    return q
imdb['Quantile_num']=imdb['title_len'].apply(names)


# In[32]:


#OUESTION 17(C):
#CROSSTAB BETWEEN QUANTILE THAT THE YEAR FALL UNDER AND MOVIE TITLE LENGTH WITH VALUES AS AVERAGE IMDB SCORE
l1=pd.crosstab(imdb.year,[imdb.Quantile_num,imdb.title_len],values=imdb.imdbRating,margins=True,aggfunc='mean')
print(l1)


# In[35]:


#QUESTION 18:
diamonds=pd.read_csv('diamonds.csv')
diamonds['volume']='None'
d1=diamonds.copy()
d1=d1.dropna()
d1=d1[d1['z']!='None']
d1['z_new'] = d1['z'].astype(float)
diamonds['volume']=d1['volume']
def volume(depth,x,y,z):
    if depth > 60:
        volume=x*y*z
    else:
        volume=8
    return volume
d1['volume']=np.vectorize(volume)(d1['depth'],d1['x'],d1['y'],d1['z_new'])
d1['bins']=pd.qcut(d1['volume'],q=6)
d1=pd.DataFrame(d1)
ll1=pd.crosstab(d1.bins, d1.cut).apply(lambda r: r/r.sum(), axis=1)
print(ll1)


# In[36]:


#QUESTION 19
imdb_quarr=pd.read_csv('movie_metadata.csv')


# In[37]:


df=imdb_quarr.copy()
#QUESTION 4
df['Action']='None'
df['Adventure']='None'
df['Animation']='None'
df['Biography']='None'
df['Comedy']='None'
df['Crime']='None'
df['Documentary']='None'
df['Drama']='None'
df['Family']='None'
df['Fantasy']='None'
df['FilmNoir']='None'
df['GameShow']='None'
df['History']='None'
df['Horror']='None'
df['Music']='None'
df['Musical']='None'
df['Mystery']='None'
df['News']='None'
df['RealityTV']='None'
df['Romance']='None'
df['SciFi']='None'
df['Short']='None'
df['Sport']='None'
df['Thriller']='None'
df['War']='None'
df['Western']='None'

# def f1(genre):
#     genre=genre.split("|")
#     return genre
# df['genres']=df['genres'].apply(f1)
def Action(x):
    if('Action' in x):
        flag=1
    else:
        flag=0
    return flag
def Adventure(x):
    if('Adventure' in x):
        flag=1
    else:
        flag=0
    return flag
def Animation(x):
    if('Animation' in x):
        flag=1
    else:
        flag=0
    return flag
def Biography(x):
    if('Biography' in x):
        flag=1
    else:
        flag=0
    return flag
def Comedy(x):
    if('Comedy' in x):
        flag=1
    else:
        flag=0
    return flag
def Crime(x):
    if('Crime' in x):
        flag=1
    else:
        flag=0
    return flag
def Documentary(x):
    if('Documentary' in x):
        flag=1
    else:
        flag=0
    return flag
def Drama(x):
    if('Drama' in x):
        flag=1
    else:
        flag=0
    return flag
def Fantasy(x):
    if('Fantasy' in x):
        flag=1
    else:
        flag=0
    return flag
def Family(x):
    if('Family' in x):
        flag=1
    else:
        flag=0
    return flag
def FilmNoir(x):
    if('Film-Noir' in x):
        flag=1
    else:
        flag=0
    return flag
def GameShow(x):
    if('Game-Show' in x):
        flag=1
    else:
        flag=0
    return flag
def History(x):
    if('History' in x):
        flag=1
    else:
        flag=0
    return flag
def Music(x):
    if('Music' in x):
        flag=1
    else:
        flag=0
    return flag
def Musical(x):
    if('Musical' in x):
        flag=1
    else:
        flag=0
    return flag
def Mystery(x):
    if('Mystery' in x):
        flag=1
    else:
        flag=0
    return flag
def News(x):
    if('News' in x):
        flag=1
    else:
        flag=0
    return flag
def Horror(x):
    if('Horror' in x):
        flag=1
    else:
        flag=0
    return flag
def Reality(x):
    if('Reality-TV' in x):
        flag=1
    else:
        flag=0
    return flag
def Romance(x):
    if('Romance' in x):
        flag=1
    else:
        flag=0
    return flag
def SCIFI(x):
    if('Sci-Fi' in x):
        flag=1
    else:
        flag=0
    return flag
def Short(x):
    if('Short' in x):
        flag=1
    else:
        flag=0
    return flag
def Sport(x):
    if('Sport' in x):
        flag=1
    else:
        flag=0
    return flag
def Thriller(x):
    if('Thriller' in x):
        flag=1
    else:
        flag=0
    return flag
def War(x):
    if('War' in x):
        flag=1
    else:
        flag=0
    return flag
def Western(x):
    if('Western' in x):
        flag=1
    else:
        flag=0
    return flag
def TalkShow(x):
    if('Talk-Show' in x):
        flag=1
    else:
        flag=0
    return flag

df['Action']=df['genres'].apply(Action)
df['Adventure']=df['genres'].apply(Adventure)
df['Animation']=df['genres'].apply(Animation)
df['Crime']=df['genres'].apply(Crime)
df['Mystery']=df['genres'].apply(Mystery)
df['Documentary']=df['genres'].apply(Documentary)
df['Family']=df['genres'].apply(Family)
df['Music']=df['genres'].apply(Music)
df['Musical']=df['genres'].apply(Musical)
df['Horror']=df['genres'].apply(Horror)
df['History']=df['genres'].apply(History)
df['Short']=df['genres'].apply(Short)
df['Sport']=df['genres'].apply(Sport)
df['War']=df['genres'].apply(War)
df['Western']=df['genres'].apply(Western)
df['Comedy']=df['genres'].apply(Comedy)
df['Drama']=df['genres'].apply(Drama)
df['Fantasy']=df['genres'].apply(Fantasy)
df['News']=df['genres'].apply(News)
df['Thriller']=df['genres'].apply(Thriller)
df['Romance']=df['genres'].apply(Romance)
df['RealityTV']=df['genres'].apply(Reality)
df['SciFi']=df['genres'].apply(SCIFI)
df['FilmNoir']=df['genres'].apply(FilmNoir)
df['GameShow']=df['genres'].apply(GameShow)
df['Biography']=df['genres'].apply(Biography)
df['TalkShow']=df['genres'].apply(TalkShow)
dfDummy=pd.DataFrame(df)
#dfDummy


# In[39]:



imdb_quar=dfDummy[(dfDummy['title_year']>=2007) & (dfDummy['title_year']<=2016)]
imdb_quar
def get_quarter(year):
    if((year>=2007) and (year<=2009)):
        quar='Quarter1'
    elif((year>2009) and (year<=2011)):
        quar='Quarter2'
    elif((year>2011 and year<=2014)):
        quar='Quarter3'
    else:
        quar='Quarter4'
    return quar
def grosss(qu):
    if(qu=='Quarter1'):
        gross=2.717576e+10
    elif(qu=='Quarter2'):
        gross=1.867685e+10
    elif(qu=='Quarter3'):
        gross=3.230455e+10
    else:
        gross=1.520631e+10
    return gross
imdb_quar['Quarter']=pd.qcut(imdb_quar['title_year'],q=4)
imdb_quar
imdb_quar['Quarter']=imdb_quar['title_year'].apply(get_quarter)
# #imdb_quar['Movies_top20']
qq=imdb_quar.groupby(['Quarter'])['imdb_score'].mean().reset_index()
qq
qq1=imdb_quar.groupby(['Quarter'])['gross'].sum().reset_index()
qq1=pd.merge(qq,qq1,on='Quarter',how='inner')
qq1
imdb_quar['grosss']=imdb_quar['Quarter'].apply(grosss)
imdb_quar=pd.DataFrame(imdb_quar)
imdbq4=imdb_quar.copy()
imdbq4.sort_values('title_year',inplace=True)
imdbq4['percent_gross']=imdbq4['gross']/imdbq4['grosss']
imdbq4.sort_values(['title_year','percent_gross'],ascending=[True,False],inplace=True)
l1=imdbq4.groupby(['Quarter'])['imdb_score'].count().reset_index()
imdbc1=imdbq4[imdbq4['Quarter']=='Quarter1'].head(67)
imdbc2=imdbq4[imdbq4['Quarter']=='Quarter2'].head(72)
imdbc3=imdbq4[imdbq4['Quarter']=='Quarter3'].head(71)
imdbc4=imdbq4[imdbq4['Quarter']=='Quarter4'].head(33)
imdbc4_final=pd.concat([imdbc1,imdbc2,imdbc3,imdbc4])
imdbc4_final.columns
d = {'imdb_score': ['mean'],'Action':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res=pd.DataFrame(imdbc4_final.groupby(['Quarter']).agg(d))
res.columns = ['_'.join(col) for col in res.columns.values]
res=pd.DataFrame(res)
print(res)


# In[40]:


imdb_new=pd.read_csv('imdb (1).csv',escapechar='\\')


# In[41]:


#QUESTION 20:
imdb_new['Decile_num']=pd.qcut(imdb_new['duration'],10,labels=False)
dk = {'nrOfWins': ['sum'], 'nrOfNominations':['sum']}
ress = imdb_new.groupby(['Decile_num']).agg(dk)
ress.columns = ['_'.join(col) for col in ress.columns.values]
ress=pd.DataFrame(ress)


# In[42]:



i1=imdb_new[imdb_new['Decile_num']==0]
i2=imdb_new[imdb_new['Decile_num']==1]
i3=imdb_new[imdb_new['Decile_num']==2]
i4=imdb_new[imdb_new['Decile_num']==3]
i5=imdb_new[imdb_new['Decile_num']==4]
i6=imdb_new[imdb_new['Decile_num']==5]
i7=imdb_new[imdb_new['Decile_num']==6]
i8=imdb_new[imdb_new['Decile_num']==7]
i9=imdb_new[imdb_new['Decile_num']==8]
i10=imdb_new[imdb_new['Decile_num']==9]

d1 = {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res1=pd.DataFrame(i1.groupby(['Decile_num']).agg(d1))
res1.columns = ['_'.join(col) for col in res1.columns.values]
res1=pd.DataFrame(res1)
res1
d2 = {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res2=pd.DataFrame(i2.groupby(['Decile_num']).agg(d2))
res2.columns = ['_'.join(col) for col in res2.columns.values]
res2=pd.DataFrame(res2)
res2
d3= {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res3=pd.DataFrame(i3.groupby(['Decile_num']).agg(d3))
res3.columns = ['_'.join(col) for col in res3.columns.values]
res3=pd.DataFrame(res3)
res3
d4= {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res4=pd.DataFrame(i4.groupby(['Decile_num']).agg(d4))
res4.columns = ['_'.join(col) for col in res4.columns.values]
res4=pd.DataFrame(res4)
res4
d5= {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res5=pd.DataFrame(i5.groupby(['Decile_num']).agg(d5))
res5.columns = ['_'.join(col) for col in res5.columns.values]
res5=pd.DataFrame(res5)
res5
d6= {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res6=pd.DataFrame(i6.groupby(['Decile_num']).agg(d6))
res6.columns = ['_'.join(col) for col in res6.columns.values]
res6=pd.DataFrame(res6)
res6
d7= {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res7=pd.DataFrame(i7.groupby(['Decile_num']).agg(d7))
res7.columns = ['_'.join(col) for col in res7.columns.values]
res7=pd.DataFrame(res7)
res7
d8= {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res8=pd.DataFrame(i8.groupby(['Decile_num']).agg(d8))
res8.columns = ['_'.join(col) for col in res8.columns.values]
res8=pd.DataFrame(res8)
res8
d9= {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res9=pd.DataFrame(i9.groupby(['Decile_num']).agg(d9))
res9.columns = ['_'.join(col) for col in res9.columns.values]
res9=pd.DataFrame(res9)
res9
d10= {'Action':['sum'],'Adult':['sum'],'TalkShow':['sum'],'Adventure':['sum'],'Animation':['sum'],'Biography':['sum'],'Comedy':['sum'],'Crime':['sum'],'Documentary':['sum'],'Drama':['sum'],'Family':['sum'],'Fantasy':['sum'],'FilmNoir':['sum'],'GameShow':['sum'],'History':['sum'],'Horror':['sum'],'Music':['sum'],'Musical':['sum'],'Mystery':['sum'],'News':['sum'],'RealityTV':['sum'],'Romance':['sum'],'SciFi':['sum'],'Short':['sum'],'Sport':['sum'],'Thriller':['sum'],'War':['sum'],'Western':['sum']}
res10=pd.DataFrame(i10.groupby(['Decile_num']).agg(d10))
res10.columns = ['_'.join(col) for col in res10.columns.values]
res10=pd.DataFrame(res10)

imdbc5_final=pd.DataFrame(pd.concat([res1,res2,res3,res4,res5,res6,res7,res8,res9,res10]))


# In[43]:


imdbc5_final = imdbc5_final.fillna(0)
# for i in range(len(imdbc5_final.index)):
#     for row in imdbc5_final.rows:
def get_name1(row):
    list7=[]
    list8=[]
    for c in imdbc5_final.columns:
        if row[c]==row[28]:            
            return c


# In[44]:


# print(len(imdbc5_final.columns))
imdbc5_final['genre']=imdbc5_final.max(axis=1)
imdbc5_final['genre1']=imdbc5_final.apply(get_name1,axis=1)


# In[45]:


def my_fun(row):
    row[row['genre1']]=0
    return row
def my_fun1(row):
    row[row['genre2_name']]=0
    return row

    


# In[47]:


imdbc4=imdbc5_final.copy()
imdbc5_final=imdbc5_final.apply(my_fun,axis=1)
imdbc6_final=imdbc5_final[['Action_sum','Adult_sum','TalkShow_sum','Adventure_sum', 'Animation_sum', 'Biography_sum',
       'Comedy_sum', 'Crime_sum', 'Documentary_sum', 'Drama_sum', 'Family_sum',
       'Fantasy_sum', 'FilmNoir_sum', 'GameShow_sum', 'History_sum',
       'Horror_sum', 'Music_sum', 'Musical_sum', 'Mystery_sum', 'News_sum',
       'RealityTV_sum', 'Romance_sum', 'SciFi_sum', 'Short_sum', 'Sport_sum',
       'Thriller_sum', 'War_sum', 'Western_sum']].copy()
imdbc6_final['genre2']=imdbc6_final.max(axis=1)
imdbc6_final['genre2_name']=imdbc6_final.apply(get_name1,axis=1)
imdbc4.drop('genre',axis=1,inplace=True)
imdbc4['genre2']=imdbc6_final['genre2_name']
imdbc6_final=imdbc6_final.apply(my_fun1,axis=1)
imdbc6_final
imdbc9=imdbc6_final[['Action_sum','Adult_sum','TalkShow_sum', 'Adventure_sum', 'Animation_sum', 'Biography_sum',
       'Comedy_sum', 'Crime_sum', 'Documentary_sum', 'Drama_sum', 'Family_sum',
       'Fantasy_sum', 'FilmNoir_sum', 'GameShow_sum', 'History_sum',
       'Horror_sum', 'Music_sum', 'Musical_sum', 'Mystery_sum', 'News_sum',
       'RealityTV_sum', 'Romance_sum', 'SciFi_sum', 'Short_sum', 'Sport_sum',
       'Thriller_sum', 'War_sum', 'Western_sum']].copy()
imdbc9['genre3']=imdbc9.max(axis=1)
imdbc9['genre3_name']=imdbc9.apply(get_name1,axis=1)
imdbc4['genre3']=imdbc9['genre3_name']
imdbc4
imdbc4.rename(columns = {'Action_sum':'Action','Adult_sum':'Adult','TalkShow_sum':'TalkShow', 'Adventure_sum':'Adventure', 'Animation_sum':'Animation', 'Biography_sum':'Biography',
       'Comedy_sum':'Comedy', 'Crime_sum':'Crime', 'Documentary_sum':'Documentary', 'Drama_sum':'Drama', 'Family_sum':'Family',
       'Fantasy_sum':'Fantasy', 'FilmNoir_sum':'FilmNoir', 'GameShow_sum':'GameShow', 'History_sum':'History',
       'Horror_sum':'History', 'Music_sum':'Music', 'Musical_sum':'Musical', 'Mystery_sum':'Mystery', 'News_sum':'News',
       'RealityTV_sum':'RealityTV', 'Romance_sum':'Romance', 'SciFi_sum':'SCIFI', 'Short_sum':'Short', 'Sport_sum':'Sport',
       'Thriller_sum':'Thriller', 'War_sum':'War', 'Western_sum':'Western'}, inplace = True)
imdbc4['nrOfWins_sum']=ress['nrOfWins_sum']
imdbc4['nrOfNominations_sum']=ress['nrOfNominations_sum']
print(imdbc4)


# In[ ]:




