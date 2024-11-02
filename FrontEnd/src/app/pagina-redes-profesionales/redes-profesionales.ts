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