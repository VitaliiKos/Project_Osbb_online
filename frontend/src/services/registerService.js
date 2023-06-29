import {apiService} from "./apiService";
import {mainUrls} from "../configs";

const registerService = {
    create:(user)=> apiService.post(mainUrls.auth.register, user)
};

export {registerService};