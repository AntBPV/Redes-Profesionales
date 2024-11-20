export class Post {
  id: number;
  user: number;
  UserProfile: number;
  EnterpriseProfile: number;
  image?: File | string;
  text: string;

  constructor(
    id: number,
    user: number,
    UserProfile: number,
    EnterpriseProfile: number,
    image: string,
    text: string
  ) {
    this.id = id;
    this.user = user;
    this.UserProfile = UserProfile;
    this.EnterpriseProfile = EnterpriseProfile;
    this.image = image;
    this.text = text;
  }
}
