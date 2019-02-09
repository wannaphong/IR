# -*- coding: utf-8 -*-
from collections import defaultdict
from pythainlp.tokenize import word_tokenize,sent_tokenize

class ir:
    """
    935308 Information Retrieval
    สาขาวิทยาการคอมพิวเตอร์และสารสนเทศ
    คณะวิทยาศาสตร์ประยุกต์และวิศวกรรมศาสตร์
    วิทยาเขตหนองคาย มหาวิทยาลัยขอนแก่น

    เขียนโดย นายวรรณพงษ์ ภัททิยไพบูลย์
    """
    def __init__(self):
        self.inv_indx = defaultdict(dict)
        self.idx=1
        self.name_docs={}
        self.idx2docs={}
    def build_data(self,list_text):
        self.loc=1
        for data in list_text:
            for word in word_tokenize(data):
                if self.idx not in self.inv_indx[word]:
                    self.inv_indx[word][self.idx]=[self.loc]
                else:
                    self.inv_indx[word][self.idx].append(self.loc)
                self.loc+=1
        self.idx+=1
    def load(self,filename,encoding="utf-8"):
        with open(filename,"r",encoding="utf-8") as f:
            self.data=f.read()
        self.content = [x.strip() for x in sent_tokenize(self.data)]
        self.build_data(self.content)
        self.name_docs[filename]=self.idx-1
        self.idx2docs=dict((v,k) for k,v in self.name_docs.items())
    def get_inv(self):
        return self.inv_indx
    def intersect(self,p1,p2):
        self.docID1 = 0
        self.docID2 = 0
        if len(p1) > 0 and len(p2) > 0:
            while self.docID1 < len(p1) and self.docID2 < len(p2):
                pass
    def process_conjunctive_query(self,query):
        self.query_terms = [t.strip() for t in query.split("AND")]
        if len(self.query_terms) == 2:
            pass
        else:
            print("Error")
    def get_doc_index(self,word):
        return self.inv_indx[word]
    def get_doc_idx(self,filename=None):
        if filename==None:
            return self.name_docs
        else:
            return self.name_docs[filename]
    def idx_to_doc(self,idx=None):
        if idx==None:
            return self.idx2docs
        else:
            return self.idx2docs[idx]
    def query(self,txt):
        pass
