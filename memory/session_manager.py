class Session_Manager:
    def __init__(self):
        self.history=[]
        self.last_query=None
        self.last_dataframe=None
    def add_user_message(self,message):
        self.history.append({
            "role":"user",
            "content":message
        })
        if len(self.history)>10:
            self.history=self.history[-10:]
    def add_assistant_message(self,message):
        self.history.append({
            "role":"assistant",
            "content":message
        })
    def get_history(self,limit=6):
        return self.history[-limit:]
    def add_last_query(self,query):
        self.last_query=query
    def get_last_query(self):
        return self.last_query
    def add_last_dataframe(self,df):
        self.last_dataframe=df
    def get_last_dataframe(self):
        return self.last_dataframe

if __name__=="__main__":
    session=Session_Manager()
    session.add_user_message("show products")
    print(session.get_history)
    session.add_last_query("show products")
    print(session.get_last_query())