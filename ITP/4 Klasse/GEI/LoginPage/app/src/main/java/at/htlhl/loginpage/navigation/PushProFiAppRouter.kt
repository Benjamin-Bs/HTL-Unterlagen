package at.htlhl.loginpage.navigation

import androidx.compose.runtime.MutableState
import androidx.compose.runtime.mutableStateOf

sealed class Screen {

    object SignUpScreen: Screen()
    object TermsAndConditionsScreen: Screen()
}

object PushProFiAppRouter {

    var currentScreen: MutableState<Screen> = mutableStateOf(Screen.SignUpScreen)

    fun navigateTo(destination: Screen){

        currentScreen.value = destination

    }

}