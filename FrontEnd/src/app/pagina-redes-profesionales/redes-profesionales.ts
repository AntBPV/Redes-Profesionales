export class user{
    username: string;
    password: string;
    email: string;
    id: number;



    public constructor(id:number, username: string,password: string, email: string){
        this.username = username;
        this.password = password;
        this.email = email;
        this.id = id;   
    }
}

export class publicaciones{
    user: string;
    image: string;
    text: string;
    id: number;
    

    public constructor(id:number, user: string,image: string, text: string){
        this.user = user;
        this.image = image;
        this.text = text;
        this.id = id;   
    }
}