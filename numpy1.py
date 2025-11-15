{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f0e22cc3-f4ef-42e4-98f2-fa10ed321c2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import sklearn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "faface90-281d-4979-8707-7a980736843a",
   "metadata": {},
   "outputs": [],
   "source": [
    "my=np.array([3,6,7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "06a80ed0-5a4a-4519-8654-a0565ac0462e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print(my[1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d2b27b9c-2208-4b97-8246-c31c41da5fa9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3,)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "093b0351-691b-4f28-9de8-041dd4dc343a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int64')"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "50decd83-8f0a-4140-87ac-0a7658773030",
   "metadata": {},
   "outputs": [],
   "source": [
    "my[1]=45"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "6e9f5b96-cc6c-4470-85f0-fd482eb1e8d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Array Creation\n",
    "\n",
    "listarray=np.array([[1,2,3],[5,6,7],[7,9,8]])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "af5d2813-3561-48db-99dd-7ff1c76b11b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [5 6 7]\n",
      " [7 9 8]]\n"
     ]
    }
   ],
   "source": [
    "print(listarray)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a38a31e4-3eae-4f16-845a-74544eabdae4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 3)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listarray.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "9fc18fbe-534f-41d2-bf4c-f805600ae96a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listarray.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "edb9a5be-2199-49f6-b949-ae5094738ffc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array({34, 71}, dtype=object)"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array({34,71})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "eaab7b29-1bd2-4914-bb5c-fe080bafa80b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Zeros Array Make\n",
    "\n",
    "ze=np.zeros((2,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7b61bdc8-eaae-4635-8b47-8a007228b1c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., 0., 0.],\n",
       "       [0., 0., 0., 0., 0.]])"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ze"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "6fedfa46-8c38-4592-9a05-6a93cb4d3275",
   "metadata": {},
   "outputs": [],
   "source": [
    "rng=np.arange(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "c7a3d04f-969b-4e6e-bfa9-cb21f9a1204a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rng"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "0fa142ac-e239-46e4-a49d-24336f46a133",
   "metadata": {},
   "outputs": [],
   "source": [
    "lspace=np.linspace(1,5,12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "be8b4355-ccc9-418c-af01-58778df6b6a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.        , 1.36363636, 1.72727273, 2.09090909, 2.45454545,\n",
       "       2.81818182, 3.18181818, 3.54545455, 3.90909091, 4.27272727,\n",
       "       4.63636364, 5.        ])"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lspace"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c08d8a41-4306-497f-b4d1-f8f520d29a2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp=np.empty((4,6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "8205ee2a-1b54-4a1b-bc9c-ee7d9233d207",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[6.23042070e-307, 4.67296746e-307, 1.69121096e-306,\n",
       "        7.56595733e-307, 1.89146896e-307, 7.56571288e-307],\n",
       "       [3.11525958e-307, 1.24610723e-306, 1.37962320e-306,\n",
       "        1.29060871e-306, 2.22518251e-306, 1.33511969e-306],\n",
       "       [1.78022342e-306, 1.05700345e-307, 3.11525958e-307,\n",
       "        1.69118108e-306, 8.06632139e-308, 1.20160711e-306],\n",
       "       [1.69119330e-306, 1.24611402e-306, 1.33512173e-306,\n",
       "        1.11261570e-306, 9.79094970e-307, 1.69119330e-306]])"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "c2360e98-6fd9-4af3-be02-73005510d46a",
   "metadata": {},
   "outputs": [],
   "source": [
    "empli=np.empty_like(lspace)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "e67ea05f-f45b-4d22-a31c-321e1c7511b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.        , 1.36363636, 1.72727273, 2.09090909, 2.45454545,\n",
       "       2.81818182, 3.18181818, 3.54545455, 3.90909091, 4.27272727,\n",
       "       4.63636364, 5.        ])"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "empli"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "84e345b3-0248-48c5-a40f-e372a63529ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "ide=np.identity(45)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "5619d853-e33c-41e7-bec3-b0619685fba8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 1., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 1., ..., 0., 0., 0.],\n",
       "       ...,\n",
       "       [0., 0., 0., ..., 1., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 1., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 1.]], shape=(45, 45))"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ide"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "c259658b-96af-4dbf-a333-22ef9a17a2e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(45, 45)"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ide.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b42f8918-b71d-4578-b3dd-306984f2ec07",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr=np.arange(99)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "84bd16d5-eab5-46ae-9d92-af9deb295917",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,\n",
       "       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,\n",
       "       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,\n",
       "       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,\n",
       "       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98])"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "f22eaaa5-d4cb-4f09-ab18-f504ec3696c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,\n",
       "        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,\n",
       "        32],\n",
       "       [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,\n",
       "        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,\n",
       "        65],\n",
       "       [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,\n",
       "        82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,\n",
       "        98]])"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.reshape(3,33)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "17d2dfd0-0155-4fe7-a1b5-d5aa5b204bf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Axis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "41a6ffbb-1544-47e3-847b-db6725882c5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=[[1,2,3],[4,5,6],[7,1,0]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "2317bfae-6020-4d2b-a50e-bbb659c65259",
   "metadata": {},
   "outputs": [],
   "source": [
    "ar=np.array(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "2c7dc489-d7e5-4249-97d8-d67add4267b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 1, 0]])"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "59e16d43-2d5e-40ad-b98f-89bd59f38a75",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([12,  8,  9])"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.sum(axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "6a92d02b-bc17-497b-a71e-ef2205e7c271",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 6, 15,  8])"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.sum(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "7e47e507-3615-4ad4-9e62-360471fd53c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 7],\n",
       "       [2, 5, 1],\n",
       "       [3, 6, 0]])"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "4769a1a8-02b8-439d-8b91-1277a5efca40",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<numpy.flatiter at 0x256cd791540>"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.flat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "2565fa37-5312-4891-badf-ecfb08a1f10f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "1\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "for item in ar.flat:\n",
    "    print(item )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "0ce287aa-ef4a-4ca2-b541-cdb36835b8b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "511f202b-9b30-420f-9c05-27d5cb6e6ba7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "c8633fd6-9c0e-4f92-8dff-d20560c79f6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "72"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.nbytes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "082429e4-88bc-403f-8ff2-a40be585409c",
   "metadata": {},
   "outputs": [],
   "source": [
    "one=np.array([1,2,3,7,8])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "5d2c2b13-f604-4761-93d1-75f2bb9ba6da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(4)"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one.argmax()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "8989f3d9-8076-4172-a189-aa1ed85209b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one.argmin()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "217ce006-480b-45e4-89db-73dfc895ff15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4])"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one.argsort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "41aef39b-4ec5-474d-b57c-5d2cac3bbd4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 1, 0]])"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "32b82d79-cf0c-4404-ae2b-ed2139f32436",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(8)"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.argmin()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "cef74523-1e77-4c29-87ec-bed5551f0483",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(6)"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.argmax()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "d775866b-09e8-404a-be74-84d8c3ebe330",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 1, 1])"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.argmax(axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "e6c81bca-a0d7-4cea-82cf-0a67282797c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 1, 2],\n",
       "       [0, 1, 2],\n",
       "       [2, 1, 0]])"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.argsort(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "ddc9578c-d90a-4f1b-bf07-fcb4fc18a46f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 2, 2],\n",
       "       [1, 0, 0],\n",
       "       [2, 1, 1]])"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.argsort(axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "545f5f79-9ec1-4eb0-a6ad-fe690ee1c5cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 5, 6, 7, 1, 0])"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.ravel()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "f850fe57-68a5-4da4-acc6-c5dde47e7f10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1],\n",
       "       [2],\n",
       "       [3],\n",
       "       [4],\n",
       "       [5],\n",
       "       [6],\n",
       "       [7],\n",
       "       [1],\n",
       "       [0]])"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.reshape(9,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "50e73b45-3fd7-4bbc-8cf2-be9dbe94ba83",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 1, 0]])"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "5e3ea07a-e88c-4630-a3b5-e63049939c2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "ar2=np.array([[1,4,7],[7,4,6],[9,6,4]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "6d6e74fd-a868-41a5-9805-ef6ab74f915d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 2,  6, 10],\n",
       "       [11,  9, 12],\n",
       "       [16,  7,  4]])"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar+ar2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "c6fbc473-4085-4d66-b87e-bae7391d1780",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  8, 21],\n",
       "       [28, 20, 36],\n",
       "       [63,  6,  0]])"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar*ar2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "8d090c99-b2b0-4711-9c7c-70573d193b79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1.        , 1.41421356, 1.73205081],\n",
       "       [2.        , 2.23606798, 2.44948974],\n",
       "       [2.64575131, 1.        , 0.        ]])"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.sqrt(ar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "f960266f-65f7-4705-948c-7378d0a8ab7f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(29)"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "3d9fdd4c-4cd9-469a-b547-e82bd1f87550",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "1fd8abe6-8e70-497f-bdb8-dfeed02fe45d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(7)"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "e6184153-ee9f-46c3-a621-da1e7773f750",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([1, 2]), array([2, 0]))"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Comparing\n",
    "\n",
    "np.where(ar>5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "77daaea5-474b-4969-8bbb-3d3314a17a7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.count_nonzero(ar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "4fbe7d96-3d1b-4545-8d75-ceb878f1833f",
   "metadata": {},
   "outputs": [],
   "source": [
    "ar[1,2]=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "2c67c1e8-f75c-43dd-a200-3c69baf34b0b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 0, 0, 1, 1, 2, 2]), array([0, 1, 2, 0, 1, 0, 1]))"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.nonzero(ar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "7d38901d-682c-4912-b9ab-97f49324228f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# System\n",
    "\n",
    "import sys\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "44e75d27-81be-45be-804f-df91b4dd7ec5",
   "metadata": {},
   "outputs": [],
   "source": [
    "ch_ar=[0,4,55,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "d49e9f15-ca5f-46f7-8411-fdc6eae389ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "np_ar =np.array(ch_ar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "35ae2574-44f9-48d9-94b1-a3fd125353ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "112"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sys.getsizeof(1)*len(np_ar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "512adb15-628e-4d59-8868-f15d1552ee16",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np_ar.itemsize*np_ar.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f93407b-41b5-45af-9896-bca8648457a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
