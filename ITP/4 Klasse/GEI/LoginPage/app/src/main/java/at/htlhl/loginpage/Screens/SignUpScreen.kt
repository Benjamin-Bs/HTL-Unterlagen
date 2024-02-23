package at.htlhl.loginpage.Screens

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import at.htlhl.loginpage.Components.ButtonComponent
import at.htlhl.loginpage.Components.CheckBoxComponent
import at.htlhl.loginpage.Components.ClickableLoginTextComponent
import at.htlhl.loginpage.Components.DividerTextComponent
import at.htlhl.loginpage.Components.HeadingTextComponent
//import at.htlhl.loginpage.Components.MyTextField
import at.htlhl.loginpage.Components.MyTextFieldComponet
import at.htlhl.loginpage.Components.NormalTextComponent
import at.htlhl.loginpage.Components.PasswordTextFieldComponent
import at.htlhl.loginpage.R
import at.htlhl.loginpage.navigation.PushProFiAppRouter
import at.htlhl.loginpage.navigation.Screen

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SignUpScreen() {

    Surface(
        color = Color.White,
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White)
            .padding(28.dp)
    ) {
        Column(
            modifier = Modifier.fillMaxSize()
        ) {

            NormalTextComponent(value = stringResource(id = R.string.hello))
            HeadingTextComponent(value = stringResource(id = R.string.create_account))
            Spacer(modifier = Modifier.height(20.dp))
            MyTextFieldComponet(
                labelValue = stringResource(id = R.string.firstname)
                /*
                , painterResource(
                id = R.drawable
            )

                 */
            )
            Spacer(modifier = Modifier.height(10.dp))
            MyTextFieldComponet(labelValue = stringResource(id = R.string.lastname))
            Spacer(modifier = Modifier.height(10.dp))
            MyTextFieldComponet(labelValue = stringResource(id = R.string.email))
            Spacer(modifier = Modifier.height(10.dp))
            PasswordTextFieldComponent(labelValue = stringResource(id = R.string.password))

            CheckBoxComponent(value = stringResource(id = R.string.terms_and_conditions),
                onTextSelected = {
                    PushProFiAppRouter.navigateTo(Screen.TermsAndConditionsScreen)
                })
            Spacer(modifier = Modifier.height(80.dp))
            ButtonComponent(value = stringResource(id = R.string.register))
            
            Spacer(modifier = Modifier.height(20.dp))

            DividerTextComponent()
            
            ClickableLoginTextComponent(onTextSelected = {

            })
        }

    }
}

@Preview
@Composable
fun DefaultPreviewOfSignUpScreen() {
    SignUpScreen()
}