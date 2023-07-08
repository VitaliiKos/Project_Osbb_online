import {apiService} from "./apiService";
import {mainUrls} from "../configs";

const newsEventsService = {
    getAll: (page = 1) => apiService.get(mainUrls.news.news, {params: {page}}),
    getById: (id) => apiService.get(mainUrls.news.byId(id)),
    add: (data) => apiService.post(`${mainUrls.news.news}/create`, data),
    deleteById: (id) => apiService.delete(mainUrls.news.byId(id)),
    updateById: (newsId, data) => apiService.patch(mainUrls.news.byId(newsId), data)
}

export {newsEventsService}