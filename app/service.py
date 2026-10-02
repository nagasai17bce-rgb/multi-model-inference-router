class Service:
 def run(self,value):
  p=[{'name':'fast-local','latency_ms':30,'cost':1.0},{'name':'quality-local','latency_ms':90,'cost':1.8}]; c=min(p,key=lambda x:x['latency_ms']+10*x['cost']); return {'selected_provider':c,'request':value,'fallback_chain':[x['name'] for x in p if x is not c]}