
import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
        usuario=UserManager()
        for i in range(1000):    
             usuario.add_user(i,f"yo soy el :{i}")
        usuario.add_user(37,"ramon")
        duplicados=[]
        for i in usuario.get_all_names():
            if usuario.get_all_names().count(i) > 1 and i not in duplicados:
                duplicados.append(i)

        print("Duplicados:", duplicados)
        start = time.time()   # inicia el timer
        print(usuario.get_all_names())
        end = time.time()
        print ("Duracion:", end - start,"segundos")