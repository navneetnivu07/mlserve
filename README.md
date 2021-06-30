# mlserve

```

conda create --name deploy Python=3.8

conda activate deploy

pip install Flask

```

```python

import pickle
 
# Save the trained model as a pickle string.
filename = 'finalized_model.pkl'
pickle.dump(model, open(filename, 'wb'))

```