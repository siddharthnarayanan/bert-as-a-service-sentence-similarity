# BERT-for sentence similarity

Bidirectional Encoder Representations from Transformers or BERT has been a popular technique in NLP since Google open sourced it in 2018. Using minimal task-specific fine-tuning efforts, researchers have been able to surpass multiple benchmarks by leveraging pre-trained models that can easily be implemented to produce state of the art results. 

![Evolution of Sentence SImilarity Models](http://siddharthnarayanan.com/wp-content/uploads/2019/09/1_hPxezDTuv308MxlX03eYtg.png)

For a detailed read, check out the [article](https://medium.com/analytics-vidhya/semantic-similarity-in-sentences-and-bert-e8d34f5a4677).

This is a simple example implementation of bert-as-a-service for sentence similarity.

1. Install the required server and client

```python
pip install bert-serving-server  # server
pip install bert-serving-client  # client, independent of `bert-serving-server`
```

2. Start the BERT service. Note that you will have to choose the correct path and pre-trained model name for BERT.

```python
bert-serving-start -model_dir /tmp/english_L-12_H-768_A-12/ -num_worker=4 
```

3. Run your test script

```python
python BERT_test.py
```

