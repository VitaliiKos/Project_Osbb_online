import {apiService} from "./apiService";
import {mainUrls} from "../configs";

const pollService = {
    getAll: (page = 1) => apiService.get(mainUrls.poll.poll, {params:{page}}),
    add: (poll) => apiService.post(`${mainUrls.poll.poll}/create`, poll),
    getById: (id) => apiService.get(mainUrls.poll.byId(id)),
    updateById: (id, data) => apiService.put(mainUrls.poll.byId(id), data),
    deleteById: (id) => apiService.delete(`${mainUrls.poll.byId(id)}/delete`),

    vote: (id, data) => apiService.post(`${mainUrls.poll.byId(id)}/vote`, data),
}

export {pollService};