import {Route, Routes} from "react-router-dom";

import {MainLayout} from "./layouts";
import {
    AboutPage,
    HomePage,
    LoginPage,
    NewsAndEventsPage,
    PageNotFound, PersonalUserPage,
    RegisterPage,
    RentAndServicesPage
} from "./pages";
import {RouterEndpoints} from "./routes";
import css from './app.module.css'

function App() {
    return (<div className={css.App}>
            <Routes>
                <Route path={RouterEndpoints.index} element={<MainLayout/>}>
                    <Route path={RouterEndpoints.index} index element={<HomePage/>}/>
                    <Route path={RouterEndpoints.osbb} index element={<AboutPage/>}/>
                    <Route path={RouterEndpoints.rent_and_services} index element={<RentAndServicesPage/>}/>
                    <Route path={RouterEndpoints.news_and_events} index element={<NewsAndEventsPage/>}/>
                    <Route path={RouterEndpoints.profile} index element={<PersonalUserPage/>}/>

                    <Route path={RouterEndpoints.login} element={<LoginPage/>}/>
                    <Route path={RouterEndpoints.register} element={<RegisterPage/>}/>
                    <Route path={RouterEndpoints.notFound} element={<PageNotFound/>}/>

                </Route>
            </Routes>

        </div>
    );
}

export default App;
