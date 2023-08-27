{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-08-27 15:55:07.252 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "def find_largest_number(a, b, c):\n",
    "    return max(a, b, c)\n",
    "\n",
    "def main():\n",
    "    st.title(\"Find the Largest Number\")\n",
    "    \n",
    "    st.write(\"Enter three numbers:\")\n",
    "    a = st.number_input(\"Enter the first number:\")\n",
    "    b = st.number_input(\"Enter the second number:\")\n",
    "    c = st.number_input(\"Enter the third number:\")\n",
    "    \n",
    "    if st.button(\"Find Largest\"):\n",
    "        largest = find_largest_number(a, b, c)\n",
    "        st.write(f\"The largest number is: {largest}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.10.7"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
