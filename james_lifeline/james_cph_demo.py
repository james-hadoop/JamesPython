import time
print (time.asctime( time.localtime(time.time()) ))

cph = CoxTimeVaryingFitter(penalizer=0.3)
df_dummy = df_dummy.dropna()
cph.fit(df= df_dummy, id_col='guid', start_col='start', stop_col='end', event_col='status', step_size=0.3, show_progress=True)
#ph假设的null hypo是变量ht(xi)/ht(xj)的曲线与时间无关。 改变结构，非线性？

print (time.asctime( time.localtime(time.time()) ))
cph.print_summary()