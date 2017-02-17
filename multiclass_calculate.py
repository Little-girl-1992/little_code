def calculate_result(data_tag, data_pred):
#利用sklearn完成多分类的测度统计，正确率，准确率	
from sklearn import metrics
	m_accuracy = metrics.accuracy_score(data_tag, data_pred)
	m_precision = metrics.precision_score(data_tag, data_pred,average = None)
	m_recall = metrics.recall_score(data_tag, data_pred,average = None)
	m_f1 = metrics.f1_score(data_tag, data_pred,average = None)
	print ('accuracy:%0.3f' % m_accuracy)
	for tag in set(data_tag):
		print ('tag :%s '%tag,
			'precision:%0.3f'%(m_precision[tag]),
			'recall:%0.3f'%(m_recall[tag]),
			'f1-score:%3f'%(m_f1[tag]))
