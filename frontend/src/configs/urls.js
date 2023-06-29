const baseURL = 'api';

const auth = '/auth';
const users = '/users';
const readings = '/readings';
const advertisement = '/advertisement';
const poll = '/poll';
const meters = '/meters';
const news = '/news';
const fault_msg = '/fault_msg';
const payment = '/payment';

const mainUrls = {
    auth: {
        login: auth,
        register: `${auth}/register`,
        refresh: `${auth}/refresh`,
        me: `${auth}/me`,
        activate: `${auth}/activate`
    },
    users: {
        users: users,
        profile: `${users}/profile`,
    },

    readings: {
        readings,
    },
    advertisement: {
        advertisement,
    },
    poll: {
        poll,
    },
    meters: {
        meters,
    },

    news: {
        news,
    },

    fault_msg: {
        fault_msg,
    },

    payment: {
        payment,
    },

}

export {baseURL, mainUrls};