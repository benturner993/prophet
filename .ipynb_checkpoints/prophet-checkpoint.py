{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "61b2d39a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-03-05 20:47:08.041 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /opt/anaconda3/lib/python3.8/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "ename": "InternalHashError",
     "evalue": "module '__main__' has no attribute '__file__'\n\nWhile caching the body of `load_data()`, Streamlit encountered an\nobject of type `builtins.function`, which it does not know how to hash.\n\n**In this specific case, it's very likely you found a Streamlit bug so please\n[file a bug report here.]\n(https://github.com/streamlit/streamlit/issues/new/choose)**\n\nIn the meantime, you can try bypassing this error by registering a custom\nhash function via the `hash_funcs` keyword in @st.cache(). For example:\n\n```\n@st.cache(hash_funcs={builtins.function: my_hash_func})\ndef my_func(...):\n    ...\n```\n\nIf you don't know where the object of type `builtins.function` is coming\nfrom, try looking at the hash chain below for an object that you do recognize,\nthen pass that to `hash_funcs` instead:\n\n```\nObject of type builtins.function: <function load_data at 0x7f8a0ee8adc0>\n```\n\nPlease see the `hash_funcs` [documentation]\n(https://docs.streamlit.io/library/advanced-features/caching#the-hash_funcs-parameter)\nfor more details.\n            ",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36mto_bytes\u001b[0;34m(self, obj, context)\u001b[0m\n\u001b[1;32m    367\u001b[0m             \u001b[0;31m# Hash the input\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 368\u001b[0;31m             \u001b[0mb\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34mb\"%s:%s\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mtname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_to_bytes\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    369\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36m_to_bytes\u001b[0;34m(self, obj, context)\u001b[0m\n\u001b[1;32m    633\u001b[0m             \u001b[0;32massert\u001b[0m \u001b[0mcode\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 634\u001b[0;31m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_file_should_be_hashed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcode\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mco_filename\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    635\u001b[0m                 \u001b[0mcontext\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_get_context\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36m_file_should_be_hashed\u001b[0;34m(self, filename)\u001b[0m\n\u001b[1;32m    409\u001b[0m         return file_util.file_is_in_folder_glob(\n\u001b[0;32m--> 410\u001b[0;31m             \u001b[0mfilepath\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_get_main_script_directory\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    411\u001b[0m         ) or file_util.file_in_pythonpath(filepath)\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36m_get_main_script_directory\u001b[0;34m()\u001b[0m\n\u001b[1;32m    720\u001b[0m         \u001b[0;31m# script path in ScriptRunner.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 721\u001b[0;31m         \u001b[0mmain_path\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m__main__\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__file__\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    722\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdirname\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmain_path\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: module '__main__' has no attribute '__file__'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mInternalHashError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-2d9a66d39507>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     28\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     29\u001b[0m \u001b[0mdata_load_state\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Loading data...'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 30\u001b[0;31m \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mload_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mselected_stock\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     31\u001b[0m \u001b[0mdata_load_state\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Loading data... done!'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     32\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/caching.py\u001b[0m in \u001b[0;36mwrapped_func\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    571\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mshow_spinner\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    572\u001b[0m             \u001b[0;32mwith\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mspinner\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 573\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mget_or_create_cached_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    574\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    575\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mget_or_create_cached_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/caching.py\u001b[0m in \u001b[0;36mget_or_create_cached_value\u001b[0;34m()\u001b[0m\n\u001b[1;32m    496\u001b[0m                 \u001b[0;31m# If we generated the key earlier we would only hash those\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    497\u001b[0m                 \u001b[0;31m# globals by name, and miss changes in their code or value.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 498\u001b[0;31m                 \u001b[0mcache_key\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_hash_func\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfunc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhash_funcs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    499\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    500\u001b[0m             \u001b[0;31m# First, get the cache that's attached to this function.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/caching.py\u001b[0m in \u001b[0;36m_hash_func\u001b[0;34m(func, hash_funcs)\u001b[0m\n\u001b[1;32m    622\u001b[0m     \u001b[0;31m# because this step will be hashing any objects referenced in the function\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    623\u001b[0m     \u001b[0;31m# body.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 624\u001b[0;31m     update_hash(\n\u001b[0m\u001b[1;32m    625\u001b[0m         \u001b[0mfunc\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    626\u001b[0m         \u001b[0mhasher\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfunc_hasher\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36mupdate_hash\u001b[0;34m(val, hasher, hash_reason, hash_source, context, hash_funcs)\u001b[0m\n\u001b[1;32m    114\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m     \u001b[0mch\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_CodeHasher\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhash_funcs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 116\u001b[0;31m     \u001b[0mch\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhasher\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mval\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    117\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    118\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36mupdate\u001b[0;34m(self, hasher, obj, context)\u001b[0m\n\u001b[1;32m    391\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhasher\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mAny\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mOptional\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mContext\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    392\u001b[0m         \u001b[0;34m\"\"\"Update the provided hasher with the hash of an object.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 393\u001b[0;31m         \u001b[0mb\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mto_bytes\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    394\u001b[0m         \u001b[0mhasher\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    395\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36mto_bytes\u001b[0;34m(self, obj, context)\u001b[0m\n\u001b[1;32m    380\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    381\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mBaseException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 382\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mInternalHashError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    383\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    384\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36mto_bytes\u001b[0;34m(self, obj, context)\u001b[0m\n\u001b[1;32m    366\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    367\u001b[0m             \u001b[0;31m# Hash the input\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 368\u001b[0;31m             \u001b[0mb\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34mb\"%s:%s\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mtname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_to_bytes\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    369\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    370\u001b[0m             \u001b[0;31m# Hmmm... It's possible that the size calculation is wrong. When we\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36m_to_bytes\u001b[0;34m(self, obj, context)\u001b[0m\n\u001b[1;32m    632\u001b[0m             \u001b[0mcode\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"__code__\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    633\u001b[0m             \u001b[0;32massert\u001b[0m \u001b[0mcode\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 634\u001b[0;31m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_file_should_be_hashed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcode\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mco_filename\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    635\u001b[0m                 \u001b[0mcontext\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_get_context\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    636\u001b[0m                 \u001b[0mdefaults\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"__defaults__\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36m_file_should_be_hashed\u001b[0;34m(self, filename)\u001b[0m\n\u001b[1;32m    408\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    409\u001b[0m         return file_util.file_is_in_folder_glob(\n\u001b[0;32m--> 410\u001b[0;31m             \u001b[0mfilepath\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_get_main_script_directory\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    411\u001b[0m         ) or file_util.file_in_pythonpath(filepath)\n\u001b[1;32m    412\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/streamlit/legacy_caching/hashing.py\u001b[0m in \u001b[0;36m_get_main_script_directory\u001b[0;34m()\u001b[0m\n\u001b[1;32m    719\u001b[0m         \u001b[0;31m# This works because we set __main__.__file__ to the\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    720\u001b[0m         \u001b[0;31m# script path in ScriptRunner.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 721\u001b[0;31m         \u001b[0mmain_path\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m__main__\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__file__\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    722\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdirname\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmain_path\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    723\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mInternalHashError\u001b[0m: module '__main__' has no attribute '__file__'\n\nWhile caching the body of `load_data()`, Streamlit encountered an\nobject of type `builtins.function`, which it does not know how to hash.\n\n**In this specific case, it's very likely you found a Streamlit bug so please\n[file a bug report here.]\n(https://github.com/streamlit/streamlit/issues/new/choose)**\n\nIn the meantime, you can try bypassing this error by registering a custom\nhash function via the `hash_funcs` keyword in @st.cache(). For example:\n\n```\n@st.cache(hash_funcs={builtins.function: my_hash_func})\ndef my_func(...):\n    ...\n```\n\nIf you don't know where the object of type `builtins.function` is coming\nfrom, try looking at the hash chain below for an object that you do recognize,\nthen pass that to `hash_funcs` instead:\n\n```\nObject of type builtins.function: <function load_data at 0x7f8a0ee8adc0>\n```\n\nPlease see the `hash_funcs` [documentation]\n(https://docs.streamlit.io/library/advanced-features/caching#the-hash_funcs-parameter)\nfor more details.\n            "
     ]
    }
   ],
   "source": [
    "# pip install streamlit fbprophet yfinance plotly\n",
    "import streamlit as st\n",
    "from datetime import date\n",
    "\n",
    "import yfinance as yf\n",
    "from fbprophet import Prophet\n",
    "from fbprophet.plot import plot_plotly\n",
    "from plotly import graph_objs as go\n",
    "\n",
    "START = \"2015-01-01\"\n",
    "TODAY = date.today().strftime(\"%Y-%m-%d\")\n",
    "\n",
    "st.title('Stock Forecast App')\n",
    "\n",
    "stocks = ('GOOG', 'AAPL', 'MSFT', 'SNP', 'BNB')\n",
    "selected_stock = st.selectbox('Select dataset for prediction', stocks)\n",
    "\n",
    "n_years = st.slider('Years of prediction:', 1, 4)\n",
    "period = n_years * 365\n",
    "\n",
    "\n",
    "@st.cache\n",
    "def load_data(ticker):\n",
    "    data = yf.download(ticker, START, TODAY)\n",
    "    data.reset_index(inplace=True)\n",
    "    return data\n",
    "\n",
    "\n",
    "data_load_state = st.text('Loading data...')\n",
    "data = load_data(selected_stock)\n",
    "data_load_state.text('Loading data... done!')\n",
    "\n",
    "st.subheader('Raw data')\n",
    "st.write(data.tail())\n",
    "\n",
    "# Plot raw data\n",
    "def plot_raw_data():\n",
    "    fig = go.Figure()\n",
    "    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name=\"stock_open\"))\n",
    "    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name=\"stock_close\"))\n",
    "    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)\n",
    "    st.plotly_chart(fig)\n",
    "\n",
    "plot_raw_data()\n",
    "\n",
    "# Predict forecast with Prophet.\n",
    "df_train = data[['Date','Close']]\n",
    "df_train = df_train.rename(columns={\"Date\": \"ds\", \"Close\": \"y\"})\n",
    "\n",
    "m = Prophet()\n",
    "m.fit(df_train)\n",
    "future = m.make_future_dataframe(periods=period)\n",
    "forecast = m.predict(future)\n",
    "\n",
    "# Show and plot forecast\n",
    "st.subheader('Forecast data')\n",
    "st.write(forecast.tail())\n",
    "    \n",
    "st.write(f'Forecast plot for {n_years} years')\n",
    "fig1 = plot_plotly(m, forecast)\n",
    "st.plotly_chart(fig1)\n",
    "\n",
    "st.write(\"Forecast components\")\n",
    "fig2 = m.plot_components(forecast)\n",
    "st.write(fig2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef69162a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
